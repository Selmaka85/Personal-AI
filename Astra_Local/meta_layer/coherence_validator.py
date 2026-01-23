# -*- coding: utf-8 -*-
"""
🔍 Coherence Validator - Validează coerența și calitatea răspunsurilor
"""

import difflib
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any


class CoherenceValidator:
    """Validator pentru coerența răspunsurilor"""
    
    def __init__(self, log_file: str = "storage/logs/coherence_validator.log"):
        self.log_path = Path(log_file)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
    
    def compare(self, outputs: List[str]) -> str:
        """
        Compară multiple output-uri și alege cel mai coerent
        """
        if len(outputs) < 2:
            if len(outputs) == 1:
                return outputs[0]
            raise ValueError("Sunt necesare minim două răspunsuri pentru comparare.")
        
        scores = []
        for i in range(len(outputs)):
            for j in range(i + 1, len(outputs)):
                ratio = difflib.SequenceMatcher(None, outputs[i], outputs[j]).ratio()
                scores.append(((i, j), ratio))
        
        if not scores:
            return outputs[0]
        
        scores.sort(key=lambda x: x[1], reverse=True)
        best_pair = scores[0]
        
        # Alege output-ul mai lung dintre cele două (presupunem că e mai complet)
        chosen_index = best_pair[0][0] if len(outputs[best_pair[0][0]]) >= len(outputs[best_pair[0][1]]) else best_pair[0][1]
        
        self._log(outputs, best_pair, chosen_index)
        
        return outputs[chosen_index]
    
    def validate(self, output: str, context: Dict[str, Any] = None) -> Dict[str, float]:
        """
        Validează un singur output și returnează scoruri
        """
        scores = {
            "length_score": min(len(output) / 100, 1.0),  # Preferă răspunsuri mai lungi
            "coherence_score": self._calculate_coherence(output),
            "completeness_score": self._calculate_completeness(output),
            "relevance_score": 0.8  # Placeholder - ar trebui comparat cu context
        }
        
        scores["total"] = sum(scores.values()) / len(scores)
        return scores
    
    def _calculate_coherence(self, text: str) -> float:
        """Calculează scorul de coerență"""
        # Verifică prezența cuvintelor de legătură
        linking_words = ["pentru că", "deoarece", "așadar", "în concluzie", "astfel", "prin urmare"]
        count = sum(1 for word in linking_words if word in text.lower())
        return min(count / 3, 1.0)
    
    def _calculate_completeness(self, text: str) -> float:
        """Calculează completitudinea răspunsului"""
        # Verifică dacă are structură (propoziții multiple, punctuație)
        sentences = text.count('.') + text.count('!') + text.count('?')
        words = len(text.split())
        
        if words == 0:
            return 0.0
        
        # Scor bazat pe raportul propoziții/cuvinte și lungime
        structure_score = min(sentences / max(words / 10, 1), 1.0)
        length_score = min(words / 50, 1.0)
        
        return (structure_score + length_score) / 2
    
    def _log(self, outputs: List[str], best_pair: tuple, chosen_index: int):
        """Loghează procesul de comparare"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "comparison": {
                "pairs": [
                    {
                        "pair": [best_pair[0][0], best_pair[0][1]],
                        "similarity": round(best_pair[1], 3)
                    }
                ],
                "chosen_index": chosen_index,
                "chosen_text": outputs[chosen_index][:120] + ("..." if len(outputs[chosen_index]) > 120 else "")
            }
        }
        
        try:
            with open(self.log_path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"⚠️ Eroare la log: {e}")


def evaluate_responses(outputs: Dict[str, str]) -> Dict[str, Any]:
    """
    Funcție helper pentru evaluarea răspunsurilor multiple
    """
    validator = CoherenceValidator()
    
    if len(outputs) == 1:
        output_text = list(outputs.values())[0]
        scores = validator.validate(output_text)
        return {
            "best_response": output_text,
            "best_model": list(outputs.keys())[0],
            "scores": {list(outputs.keys())[0]: scores}
        }
    
    # Compară multiple output-uri
    output_list = list(outputs.values())
    best_output = validator.compare(output_list)
    
    # Găsește modelul corespunzător
    best_model = None
    for model, output in outputs.items():
        if output == best_output:
            best_model = model
            break
    
    if not best_model:
        best_model = list(outputs.keys())[0]
    
    # Calculează scoruri pentru toate
    all_scores = {}
    for model, output in outputs.items():
        all_scores[model] = validator.validate(output)
    
    return {
        "best_response": best_output,
        "best_model": best_model,
        "scores": all_scores
    }
