# -*- coding: utf-8 -*-
"""
🧩 Meta Reflector - Analiză metacognitivă a output-urilor
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


class MetaReflector:
    """Reflector metacognitiv pentru analiza output-urilor"""
    
    def __init__(self, log_path: str = "storage/logs/meta_reflector.log"):
        self.log_file = Path(log_path)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
    
    def analyze(self, model_outputs: Dict[str, str]) -> List[Dict[str, Any]]:
        """
        Analizează output-urile multiple și returnează reflectări
        """
        reflections = []
        
        for model, text in model_outputs.items():
            length = len(text)
            
            # Scor logic (cuvinte de legătură, structură)
            logic_score = sum(
                1 for c in ["pentru că", "deoarece", "așadar", "în concluzie", "astfel", "prin urmare"]
                if c in text.lower()
            )
            
            # Scor afectiv (cuvinte emoționale)
            affect_keywords = ["simt", "emoție", "dor", "iubire", "suflet", "inimă", "sentiment"]
            affect_score = sum(1 for keyword in affect_keywords if keyword in text.lower())
            
            # Scor poetic (cuvinte stilistice)
            poetic_keywords = ["liniște", "umbra", "ecou", "șoaptă", "stea", "infinit", "tăcere"]
            poetic_tone = any(word in text.lower() for word in poetic_keywords)
            
            # Scor tehnic (termeni tehnici)
            tech_keywords = ["funcție", "algoritm", "sistem", "proces", "structură", "implementare"]
            tech_score = sum(1 for keyword in tech_keywords if keyword in text.lower())
            
            reflections.append({
                "model": model,
                "length": length,
                "logic_score": logic_score,
                "affect_score": affect_score,
                "poetic_tone": poetic_tone,
                "tech_score": tech_score,
                "summary": text[:100] + ("..." if len(text) > 100 else "")
            })
        
        self._log_reflection(reflections)
        return reflections
    
    def _log_reflection(self, reflections: List[Dict[str, Any]]):
        """Loghează reflectările"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "reflections": reflections
        }
        
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"⚠️ Eroare la log reflectare: {e}")


# Pentru compatibilitate cu codul existent
MetaReflector = MetaReflector
