# -*- coding: utf-8 -*-
"""
🧠 Astra Thought Engine - Motorul de gândire logică și afectivă
"""

from typing import Dict, Any, List
import json
from pathlib import Path


class AstraThoughtEngine:
    """Motorul principal de gândire al Astrei"""
    
    def __init__(self):
        self.memory_path = Path("storage/memory_cache.json")
        self.thoughts_history = []
    
    def process_thought(self, input_text: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Procesează un gând și returnează analiza
        """
        thought = {
            "input": input_text,
            "context": context or {},
            "analysis": self._analyze_input(input_text),
            "emotional_weight": self._calculate_emotional_weight(input_text),
            "logical_structure": self._extract_logical_structure(input_text)
        }
        
        self.thoughts_history.append(thought)
        self._save_thoughts()
        
        return thought
    
    def _analyze_input(self, text: str) -> Dict[str, Any]:
        """Analizează inputul"""
        return {
            "length": len(text),
            "word_count": len(text.split()),
            "has_question": "?" in text,
            "has_emotion": any(word in text.lower() for word in ["simt", "dor", "iubire", "trist"]),
            "has_code": any(word in text.lower() for word in ["cod", "funcție", "clasă", "def "])
        }
    
    def _calculate_emotional_weight(self, text: str) -> float:
        """Calculează greutatea emoțională"""
        emotional_words = ["simt", "dor", "iubire", "suflet", "inimă", "emoție", "sentiment"]
        count = sum(1 for word in emotional_words if word in text.lower())
        return min(count / 3, 1.0)
    
    def _extract_logical_structure(self, text: str) -> Dict[str, Any]:
        """Extrage structura logică"""
        return {
            "has_structure": "." in text or "?" in text or "!" in text,
            "sentence_count": text.count(".") + text.count("!") + text.count("?"),
            "complexity": "complex" if len(text.split()) > 20 else "simple"
        }
    
    def _save_thoughts(self):
        """Salvează gândurile în memorie"""
        try:
            self.memory_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.memory_path, 'w', encoding='utf-8') as f:
                json.dump(self.thoughts_history[-50:], f, ensure_ascii=False, indent=2)  # Păstrează ultimele 50
        except Exception as e:
            print(f"⚠️ Eroare la salvare gânduri: {e}")
