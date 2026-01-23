# -*- coding: utf-8 -*-
"""
🧠 LLM Base - Clasă de bază pentru toate modulele LLM
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import os


class LLMBase(ABC):
    """Clasă de bază abstractă pentru toate LLM-urile"""
    
    def __init__(self, model_name: str, model_type: str = "general"):
        self.model_name = model_name
        self.model_type = model_type
        self.model = None
        self.is_loaded = False
        self.use_real_model = self._check_real_model_available()
    
    def _check_real_model_available(self) -> bool:
        """Verifică dacă modelul real este disponibil"""
        # Verifică variabile de mediu sau fișiere de configurare
        env_var = os.getenv(f"{self.model_name.upper()}_MODEL_PATH")
        return env_var is not None and os.path.exists(env_var)
    
    @abstractmethod
    def _load_real_model(self):
        """Încarcă modelul real (de implementat în subclase)"""
        pass
    
    @abstractmethod
    def _generate_real(self, prompt: str, **kwargs) -> str:
        """Generează răspuns folosind modelul real"""
        pass
    
    def _generate_mock(self, prompt: str) -> str:
        """Generează răspuns mock"""
        return f"[{self.model_name} Mock] Răspuns pentru: '{prompt[:50]}...'"
    
    def generate(self, prompt: str, max_tokens: int = 500, **kwargs) -> str:
        """
        Generează răspuns - folosește model real dacă disponibil, altfel mock
        """
        if self.use_real_model:
            try:
                if not self.is_loaded:
                    self._load_real_model()
                return self._generate_real(prompt, max_tokens=max_tokens, **kwargs)
            except Exception as e:
                print(f"⚠️ Eroare la model real {self.model_name}: {e}")
                print("   Folosind mock...")
                return self._generate_mock(prompt)
        else:
            return self._generate_mock(prompt)
    
    def load(self):
        """Încarcă modelul explicit"""
        if self.use_real_model and not self.is_loaded:
            self._load_real_model()
