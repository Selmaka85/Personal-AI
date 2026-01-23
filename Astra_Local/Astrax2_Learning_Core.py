# -*- coding: utf-8 -*-
"""
📚 Astrax2 Learning Core – Modul de auto-învățare locală
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List


class Astrax2Learning:
    """Modul de învățare pentru AstraX2"""
    
    def __init__(self):
        self.learning_log = Path("storage/logs/astrax2_learning_history.json")
        self.learning_log.parent.mkdir(parents=True, exist_ok=True)
        self.memory = self._load_memory()
    
    def _load_memory(self) -> List[Dict[str, Any]]:
        """Încarcă memoria de învățare"""
        if self.learning_log.exists():
            try:
                with open(self.learning_log, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return []
        return []
    
    def register_result(self, task_prompt: str, scores: Dict[str, Any], best_model: str):
        """
        Înregistrează rezultatul unui task pentru învățare
        """
        record = {
            "timestamp": datetime.now().isoformat(),
            "task": task_prompt,
            "scores": scores,
            "selected_model": best_model
        }
        
        self.memory.append(record)
        self.save()
    
    def save(self):
        """Salvează memoria"""
        try:
            with open(self.learning_log, 'w', encoding='utf-8') as f:
                json.dump(self.memory[-500:], f, ensure_ascii=False, indent=2)  # Păstrează ultimele 500
        except Exception as e:
            print(f"⚠️ Eroare la salvare învățare: {e}")
    
    def analyze_trends(self) -> List[tuple]:
        """Analizează tendințele de selecție a modelelor"""
        trends = {}
        for entry in self.memory:
            model = entry.get("selected_model", "unknown")
            trends[model] = trends.get(model, 0) + 1
        
        return sorted(trends.items(), key=lambda x: x[1], reverse=True)
