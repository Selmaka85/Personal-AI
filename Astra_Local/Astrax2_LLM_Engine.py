# -*- coding: utf-8 -*-
"""
🧬 Astrax2 LLM Engine - Manager pentru decizii logice prin LLM stratificat
"""

from typing import Dict, Any, List
from core_router.routing_manager import RoutingManager
from meta_layer.coherence_validator import evaluate_responses


class Astrax2Engine:
    """Engine principal AstraX2"""
    
    def __init__(self):
        self.models = self._init_models()
        self.routing_manager = None
    
    def _init_models(self) -> Dict[str, Any]:
        """Inițializează modelele"""
        from llm_modules.mistral import MistralLLM
        from llm_modules.qwen import QwenLLM
        from llm_modules.deepseek import DeepSeekLLM
        from llm_modules.mythomax import MythoMaxLLM
        from llm_modules.wizardcoder import WizardCoderLLM
        from llm_modules.codestral import CodestralLLM
        from llm_modules.mixtral import MixtralLLM
        from llm_modules.gpt4all import GPT4AllLLM
        
        return {
            "mistral": MistralLLM(),
            "qwen": QwenLLM(),
            "deepseek": DeepSeekLLM(),
            "mytho": MythoMaxLLM(),
            "wizard": WizardCoderLLM(),
            "codestral": CodestralLLM(),
            "mixtral": MixtralLLM(),
            "gpt4all": GPT4AllLLM()
        }
    
    def execute_task(self, task_prompt: str) -> Dict[str, Any]:
        """
        Execută un task folosind routing inteligent
        """
        if not self.routing_manager:
            self.routing_manager = RoutingManager(self.models)
        
        # Selectează modelele potrivite
        selected_llm = self.routing_manager.direct_to_llm(task_prompt)
        
        # Generează output
        try:
            output = selected_llm.generate(task_prompt)
            outputs = {self.routing_manager.last_model: output}
        except Exception as e:
            outputs = {"error": str(e)}
        
        # Evaluează răspunsurile
        scored_output = evaluate_responses(outputs)
        
        return scored_output
