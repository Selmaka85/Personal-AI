# -*- coding: utf-8 -*-
"""
🌊 Mistral LLM Real - Conectare la model Mistral real
"""

from llm_connector import create_real_llm, LLMConnector
from typing import Optional


class MistralLLMReal:
    """Wrapper pentru Mistral cu conectare reală"""
    
    def __init__(self, model_path: Optional[str] = None, model_type: str = "auto"):
        self.connector = LLMConnector(model_type=model_type, model_path=model_path)
        self.name = "Mistral"
        self.model_type = self.connector.model_type
    
    def generate(self, prompt: str, max_tokens: int = 500) -> str:
        """Generează răspuns folosind model real sau mock"""
        return self.connector.generate(prompt, max_tokens=max_tokens)


# Pentru compatibilitate cu codul existent
class MistralLLM(MistralLLMReal):
    """Alias pentru compatibilitate"""
    pass
