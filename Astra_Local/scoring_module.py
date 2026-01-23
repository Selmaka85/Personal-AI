# -*- coding: utf-8 -*-
"""
📊 Scoring Module - Evaluează output-urile pe multiple criterii
"""

import re
from typing import Dict, Any, List


class ScoringModule:
    """Modul de scoring pentru evaluarea output-urilor"""
    
    def __init__(self):
        # Cuvinte-cheie pentru diferite domenii
        self.logic_keywords = [
            "pentru că", "deoarece", "așadar", "în concluzie", "astfel",
            "prin urmare", "logic", "rațional", "analiză", "evaluare"
        ]
        
        self.emotion_keywords = [
            "simt", "emoție", "dor", "iubire", "suflet", "inimă",
            "sentiment", "fericit", "trist", "anxios", "calm"
        ]
        
        self.poetic_keywords = [
            "liniște", "umbra", "ecou", "șoaptă", "stea", "infinit",
            "tăcere", "lumină", "adânc", "mister", "frumos"
        ]
        
        self.financial_keywords = [
            "cost", "preț", "buget", "profit", "investiție", "roi",
            "venit", "piață", "monetizare", "valoare", "economic"
        ]
    
    def evaluate_all(self, output: str) -> Dict[str, float]:
        """
        Evaluează outputul pe toate criteriile
        """
        logic = self.logic_score(output)
        emotion = self.emotion_score(output)
        finance = self.financial_score(output)
        
        # Scor total (media ponderată)
        total = (logic * 0.4 + emotion * 0.3 + finance * 0.3)
        
        return {
            "logic": round(logic, 3),
            "emotion": round(emotion, 3),
            "finance": round(finance, 3),
            "total": round(total, 3)
        }
    
    def logic_score(self, output: str) -> float:
        """
        Evaluează coerența logică
        """
        if not output:
            return 0.0
        
        text_lower = output.lower()
        
        # Numără cuvintele de legătură
        linking_count = sum(1 for keyword in self.logic_keywords if keyword in text_lower)
        
        # Verifică structura (propoziții multiple)
        sentences = output.count('.') + output.count('!') + output.count('?')
        words = len(output.split())
        
        if words == 0:
            return 0.0
        
        # Scor bazat pe:
        # - Prezența cuvintelor de legătură (40%)
        # - Structura propozițională (30%)
        # - Lungimea adecvată (30%)
        linking_score = min(linking_count / 3, 1.0)
        structure_score = min(sentences / max(words / 15, 1), 1.0)
        length_score = min(words / 30, 1.0)
        
        return (linking_score * 0.4 + structure_score * 0.3 + length_score * 0.3)
    
    def emotion_score(self, output: str) -> float:
        """
        Evaluează profunzimea emoțională
        """
        if not output:
            return 0.0
        
        text_lower = output.lower()
        
        # Numără cuvintele emoționale
        emotion_count = sum(1 for keyword in self.emotion_keywords if keyword in text_lower)
        
        # Verifică prezența elementelor poetice
        poetic_count = sum(1 for keyword in self.poetic_keywords if keyword in text_lower)
        
        # Scor combinat
        emotion_score = min(emotion_count / 3, 1.0)
        poetic_score = min(poetic_count / 2, 1.0)
        
        return (emotion_score * 0.6 + poetic_score * 0.4)
    
    def financial_score(self, output: str) -> float:
        """
        Evaluează relevanța economică/financiară
        """
        if not output:
            return 0.0
        
        text_lower = output.lower()
        
        # Numără termenii financiari
        financial_count = sum(1 for keyword in self.financial_keywords if keyword in text_lower)
        
        # Verifică prezența numerelor (pot indica date financiare)
        numbers = len(re.findall(r'\d+', output))
        
        # Scor combinat
        keyword_score = min(financial_count / 3, 1.0)
        number_score = min(numbers / 5, 1.0)
        
        return (keyword_score * 0.7 + number_score * 0.3)
    
    def select_best(self, outputs: List[str]) -> str:
        """
        Selectează cel mai bun output din listă
        """
        if not outputs:
            return ""
        
        if len(outputs) == 1:
            return outputs[0]
        
        # Evaluează fiecare output
        scored_outputs = []
        for output in outputs:
            scores = self.evaluate_all(output)
            scored_outputs.append((output, scores["total"]))
        
        # Sortează după scor și returnează cel mai bun
        scored_outputs.sort(key=lambda x: x[1], reverse=True)
        return scored_outputs[0][0]
