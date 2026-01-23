# -*- coding: utf-8 -*-
"""
🧠 Routing Manager - Direcționează cererile către LLM-urile potrivite
"""

import re
from typing import Dict, Any, Optional


class RoutingManager:
    """Manager pentru rutarea inteligentă către LLM-uri"""
    
    def __init__(self, llm_pool: Dict[str, Any]):
        self.llm_pool = llm_pool
        self.last_model = None
        self.routing_history = []
        
        # Pattern-uri pentru detectare intenție
        self.patterns = {
            "code": [
                r"\b(cod|funcție|clasă|program|script|api|backend|frontend|debug|bug|error)\b",
                r"\b(python|javascript|typescript|java|c\+\+|sql|html|css)\b",
                r"\b(mvp|aplicație|app|website|server|database)\b"
            ],
            "strategy": [
                r"\b(plan|strategie|mvp|startup|business|afacere|piață|monetizare)\b",
                r"\b(analiză|analiza|evaluare|scor|predicție|previziune)\b"
            ],
            "emotion": [
                r"\b(simt|emoție|sentiment|dor|iubire|trist|fericit|anxios)\b",
                r"\b(poezie|poetic|frumos|artistic|creativ)\b",
                r"\b(intim|erotic|senzual|romantic)\b"
            ],
            "video": [
                r"\b(video|clip|youtube|tiktok|reels|film|scenariu|scenă)\b",
                r"\b(imagine|grafic|animat|montaj|editare)\b"
            ],
            "book": [
                r"\b(carte|capitol|poveste|narațiune|epub|pdf|audiobook)\b",
                r"\b(scrie|generează|crează).*\b(carte|poveste|roman)\b"
            ],
            "prediction": [
                r"\b(predicție|previziune|prognoză|meci|sport|fotbal)\b",
                r"\b(șansă|probabilitate|odds|cota)\b"
            ]
        }
    
    def direct_to_llm(self, input_data: str) -> Any:
        """
        Direcționează inputul către LLM-ul potrivit
        """
        intent = self._detect_intent(input_data)
        model_name = self._select_model(intent, input_data)
        
        self.last_model = model_name
        self.routing_history.append({
            "input": input_data[:100],
            "intent": intent,
            "model": model_name
        })
        
        return self.llm_pool.get(model_name, self.llm_pool.get("default"))
    
    def _detect_intent(self, text: str) -> str:
        """Detectează intenția din text"""
        text_lower = text.lower()
        scores = {}
        
        for intent, patterns in self.patterns.items():
            score = 0
            for pattern in patterns:
                matches = len(re.findall(pattern, text_lower, re.IGNORECASE))
                score += matches
            scores[intent] = score
        
        # Găsește intent-ul cu cel mai mare scor
        if scores:
            max_intent = max(scores.items(), key=lambda x: x[1])
            if max_intent[1] > 0:
                return max_intent[0]
        
        return "default"
    
    def _select_model(self, intent: str, context: str) -> str:
        """Selectează modelul potrivit pe baza intent-ului"""
        model_mapping = {
            "code": "wizardcoder",  # sau "codestral" pentru cod avansat
            "strategy": "deepseek",  # sau "mixtral" pentru strategie complexă
            "emotion": "qwen",  # sau "mythomax" pentru poetic
            "video": "qwen",  # pentru scenarii
            "book": "qwen",  # pentru narativ
            "prediction": "deepseek",  # pentru logică
            "default": "mistral"  # fallback rapid
        }
        
        # Logică avansată pentru selecție
        if intent == "code":
            # Dacă e cod complex sau MVP
            if any(word in context.lower() for word in ["mvp", "aplicație", "complet", "full"]):
                return "codestral"
            return "wizardcoder"
        
        elif intent == "strategy":
            # Pentru strategie complexă
            if any(word in context.lower() for word in ["plan", "strategie", "analiză"]):
                return "mixtral"
            return "deepseek"
        
        elif intent == "emotion":
            # Pentru conținut erotic/explicit
            if any(word in context.lower() for word in ["erotic", "senzual", "intim"]):
                return "qwen"  # Qwen e bun pentru afectiv
            return "mythomax"
        
        return model_mapping.get(intent, "mistral")
    
    def fallback_logic(self, input_data: str) -> Any:
        """Logică de fallback dacă modelul principal eșuează"""
        # Încearcă cu backup
        backup_model = self.llm_pool.get("backup")
        if backup_model:
            return backup_model
        
        # Ultimul fallback
        return self.llm_pool.get("default")
    
    def decide_pilon(self, interpreted: Dict[str, Any]) -> str:
        """
        Decide care pilon Nexus să fie activat
        """
        intent = interpreted.get("type", "generic")
        
        pilon_mapping = {
            "code": "codecore",
            "strategy": "buildcore",
            "emotion": "soulcore",
            "video": "vidcore",
            "book": "bookcore",
            "prediction": "predcore",
            "default": "soulcore"
        }
        
        return pilon_mapping.get(intent, "soulcore")
