# -*- coding: utf-8 -*-
"""
🔄 GPT4All LLM Module - Model de fallback și stabilitate
"""

import random
from typing import Optional


class GPT4AllLLM:
    """Wrapper pentru GPT4All"""
    
    def __init__(self):
        self.name = "GPT4All"
        self.model_type = "fallback-stable"
    
    def generate(self, prompt: str, max_tokens: int = 500) -> str:
        """
        Generează răspuns folosind GPT4All ca fallback
        """
        responses = [
            f"Ca model de fallback, analizez '{prompt[:40]}...' și ofer un răspuns stabil și echilibrat bazat pe principii generale.",
            f"În calitate de backup, pentru '{prompt[:35]}...' pot oferi o perspectivă generală și stabilă care poate servi ca bază pentru analize mai avansate.",
            f"Răspuns fallback pentru '{prompt[:30]}...': abordare conservatoare și stabilă care asigură funcționalitate de bază."
        ]
        
        return random.choice(responses) + "\n\n[Mock Response - Conectează la GPT4All real]"
