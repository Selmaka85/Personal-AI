# -*- coding: utf-8 -*-
"""
🧠 Nexus EFE Core Engine - Motorul central de decizie și evaluare
"""

from typing import Dict, Any, Optional
from core_router.routing_manager import RoutingManager
from scoring_module import ScoringModule
from meta_layer.coherence_validator import CoherenceValidator
from logger import Logger


class InputInterface:
    """Interfață pentru parsarea input-ului"""
    
    def parse(self, input_data: str) -> Dict[str, Any]:
        """
        Parsează inputul și extrage tipul și conținutul
        """
        return {
            "type": "generic",
            "content": input_data,
            "length": len(input_data),
            "has_question": "?" in input_data
        }


class LocalFilterEngine:
    """Filtru local pentru output-uri"""
    
    def evaluate_output(self, output: str) -> str:
        """
        Evaluează și filtrează outputul local
        """
        # Filtrare de bază pentru conținut suspect
        toxic_keywords = ["destroy", "kill", "bypass", "leak", "nuke", "hack"]
        output_lower = output.lower()
        
        for keyword in toxic_keywords:
            if keyword in output_lower:
                return "[Output filtrat din motive de securitate]"
        
        return output


class GlobalFilterEngine:
    """Filtru global pentru selecția finală"""
    
    def __init__(self, scoring_module: ScoringModule):
        self.scoring_module = scoring_module
    
    def select_best(self, outputs: list) -> str:
        """
        Selectează cel mai bun output din listă
        """
        if not outputs:
            return ""
        
        return self.scoring_module.select_best(outputs)


class ContextualMemory:
    """Memorie contextuală pentru preferințe utilizator"""
    
    def __init__(self):
        self.user_preferences = {}
    
    def load_context(self, user_id: str) -> Dict[str, Any]:
        """Încarcă contextul utilizatorului"""
        return self.user_preferences.get(user_id, {
            "preferred_tone": "poetic",
            "preferred_length": "medium"
        })
    
    def save_preference(self, user_id: str, preference: Dict[str, Any]):
        """Salvează preferința utilizatorului"""
        if user_id not in self.user_preferences:
            self.user_preferences[user_id] = {}
        self.user_preferences[user_id].update(preference)


class DecisionProtocol:
    """Protocol de decizie finală"""
    
    def __init__(self, threshold: float = 0.75):
        self.threshold = threshold
    
    def finalize(self, best_output: str, scores: Dict[str, float]) -> Optional[str]:
        """
        Finalizează decizia și returnează outputul sau None dacă e prea slab
        """
        total_score = scores.get("total", 0.0)
        
        if total_score >= self.threshold:
            return best_output
        else:
            return None  # Va declanșa rerutare


class NexusEFE:
    """
    Clasa principală Nexus EFE Core Engine
    """
    
    def __init__(self, config: Dict[str, Any], llm_pool: Dict[str, Any]):
        self.config = config
        self.thresholds = config.get("thresholds", {"accept": 0.75})
        
        # Inițializare componente
        self.input_parser = InputInterface()
        self.router = RoutingManager(llm_pool)
        self.scorer = ScoringModule()
        self.lfe = LocalFilterEngine()
        self.gfe = GlobalFilterEngine(self.scorer)
        self.memory = ContextualMemory()
        self.decision = DecisionProtocol(self.thresholds.get("accept", 0.75))
        self.logger = Logger()
    
    def process(self, input_data: str, user_id: str = "default") -> str:
        """
        Procesează inputul complet prin pipeline-ul EFE
        """
        # 1. Parsare input
        parsed = self.input_parser.parse(input_data)
        
        # 2. Rutare către LLM potrivit
        target_llm = self.router.direct_to_llm(input_data)
        
        # 3. Generare output
        try:
            raw_output = target_llm.generate(parsed["content"])
        except Exception as e:
            # Fallback dacă modelul principal eșuează
            raw_output = self.router.fallback_logic(input_data).generate(parsed["content"])
        
        # 4. Filtrare locală
        filtered_output = self.lfe.evaluate_output(raw_output)
        
        # 5. Scoring
        scores = self.scorer.evaluate_all(filtered_output)
        
        # 6. Decizie finală
        final_output = self.decision.finalize(filtered_output, scores)
        
        # 7. Dacă scorul e prea mic, încercă rerutare
        if final_output is None:
            # Rerutare cu alt model
            fallback_llm = self.router.fallback_logic(input_data)
            try:
                fallback_output = fallback_llm.generate(parsed["content"])
                fallback_filtered = self.lfe.evaluate_output(fallback_output)
                fallback_scores = self.scorer.evaluate_all(fallback_filtered)
                
                if fallback_scores.get("total", 0) >= self.thresholds.get("accept", 0.75):
                    final_output = fallback_filtered
                else:
                    final_output = "[Răspunsul nu a atins pragul minim de calitate]"
            except Exception:
                final_output = "[Eroare la generare răspuns]"
        
        # 8. Logging
        self.logger.save_logs(input_data, final_output, scores)
        
        return final_output
