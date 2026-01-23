# -*- coding: utf-8 -*-
"""
🔄 Astra Auto Improve - Sistem de auto-îmbunătățire
"""

import json
from pathlib import Path
from typing import Dict, Any, List


class AstraAutoImprove:
    """Sistem de auto-îmbunătățire pentru Astra"""
    
    def __init__(self):
        self.learning_path = Path("storage/logs/auto_improve.json")
        self.improvements = []
    
    def register_feedback(self, input_text: str, output: str, score: float, 
                         feedback: str = None):
        """
        Înregistrează feedback pentru îmbunătățire
        """
        improvement = {
            "input": input_text,
            "output": output,
            "score": score,
            "feedback": feedback,
            "timestamp": str(Path(__file__).stat().st_mtime)  # Simplificat
        }
        
        self.improvements.append(improvement)
        self._save_improvements()
        
        # Dacă scorul e prea mic, analizează și sugerează îmbunătățiri
        if score < 0.7:
            return self._analyze_improvement(improvement)
        
        return None
    
    def _analyze_improvement(self, improvement: Dict[str, Any]) -> Dict[str, Any]:
        """Analizează și sugerează îmbunătățiri"""
        suggestions = {
            "increase_length": len(improvement["output"]) < 50,
            "add_structure": "." not in improvement["output"],
            "improve_tone": improvement.get("score", 0) < 0.6
        }
        
        return {
            "suggestions": suggestions,
            "priority": "high" if improvement.get("score", 0) < 0.5 else "medium"
        }
    
    def _save_improvements(self):
        """Salvează îmbunătățirile"""
        try:
            self.learning_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.learning_path, 'w', encoding='utf-8') as f:
                json.dump(self.improvements[-100:], f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ Eroare la salvare îmbunătățiri: {e}")
