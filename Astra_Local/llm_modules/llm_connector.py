# -*- coding: utf-8 -*-
"""
🔌 LLM Connector - Conector universal pentru modele LLM reale
"""

import os
from typing import Optional, Dict, Any
from pathlib import Path


class LLMConnector:
    """Conector universal pentru diferite tipuri de modele LLM"""
    
    def __init__(self, model_type: str = "auto", model_path: Optional[str] = None):
        self.model_type = model_type
        self.model_path = model_path
        self.model = None
        self._detect_and_load()
    
    def _detect_and_load(self):
        """Detectează și încarcă modelul disponibil"""
        # Încearcă să detecteze ce tip de model este disponibil
        if self.model_type == "auto":
            # Auto-detectare
            if self._check_llama_cpp():
                self.model_type = "llama_cpp"
            elif self._check_gpt4all():
                self.model_type = "gpt4all"
            elif self._check_transformers():
                self.model_type = "transformers"
            else:
                self.model_type = "mock"
        
        # Încarcă modelul corespunzător
        if self.model_type == "llama_cpp":
            self._load_llama_cpp()
        elif self.model_type == "gpt4all":
            self._load_gpt4all()
        elif self.model_type == "transformers":
            self._load_transformers()
        else:
            self.model_type = "mock"
    
    def _check_llama_cpp(self) -> bool:
        """Verifică dacă llama-cpp-python este disponibil"""
        try:
            import llama_cpp
            return True
        except ImportError:
            return False
    
    def _check_gpt4all(self) -> bool:
        """Verifică dacă GPT4All este disponibil"""
        try:
            import gpt4all
            return True
        except ImportError:
            return False
    
    def _check_transformers(self) -> bool:
        """Verifică dacă transformers este disponibil"""
        try:
            import transformers
            return True
        except ImportError:
            return False
    
    def _load_llama_cpp(self):
        """Încarcă model folosind llama-cpp-python"""
        try:
            from llama_cpp import Llama
            
            if not self.model_path:
                # Caută modele în directorul standard
                models_dir = Path("models")
                if models_dir.exists():
                    gguf_files = list(models_dir.glob("*.gguf"))
                    if gguf_files:
                        self.model_path = str(gguf_files[0])
            
            if self.model_path and Path(self.model_path).exists():
                self.model = Llama(
                    model_path=self.model_path,
                    n_ctx=2048,
                    n_threads=4,
                    verbose=False
                )
                print(f"[INFO] Model llama-cpp încărcat: {self.model_path}")
            else:
                print("[WARNING] Nu s-a găsit model GGUF. Folosind mock.")
                self.model_type = "mock"
        except Exception as e:
            print(f"[WARNING] Eroare la încărcare llama-cpp: {e}")
            self.model_type = "mock"
    
    def _load_gpt4all(self):
        """Încarcă model folosind GPT4All"""
        try:
            from gpt4all import GPT4All
            
            if not self.model_path:
                # Modele GPT4All standard
                self.model_path = "mistral-7b-instruct-v0.1.Q4_0.gguf"
            
            self.model = GPT4All(model_name=self.model_path)
            print(f"[INFO] Model GPT4All încărcat: {self.model_path}")
        except Exception as e:
            print(f"[WARNING] Eroare la încărcare GPT4All: {e}")
            self.model_type = "mock"
    
    def _load_transformers(self):
        """Încarcă model folosind transformers"""
        try:
            from transformers import AutoModelForCausalLM, AutoTokenizer
            import torch
            
            if not self.model_path:
                # Model default mic pentru testare
                self.model_path = "microsoft/DialoGPT-small"
            
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_path,
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
            )
            print(f"[INFO] Model transformers încărcat: {self.model_path}")
        except Exception as e:
            print(f"[WARNING] Eroare la încărcare transformers: {e}")
            self.model_type = "mock"
    
    def generate(self, prompt: str, max_tokens: int = 500, temperature: float = 0.7) -> str:
        """Generează răspuns folosind modelul încărcat"""
        if self.model_type == "mock" or self.model is None:
            return f"[Mock Response] {prompt[:50]}... [Conectează un model real pentru răspunsuri reale]"
        
        try:
            if self.model_type == "llama_cpp":
                response = self.model(
                    prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    stop=["\n\n", "Human:", "User:"],
                    echo=False
                )
                return response['choices'][0]['text'].strip()
            
            elif self.model_type == "gpt4all":
                response = self.model.generate(
                    prompt,
                    max_tokens=max_tokens,
                    temp=temperature
                )
                return response.strip()
            
            elif self.model_type == "transformers":
                inputs = self.tokenizer.encode(prompt, return_tensors="pt")
                outputs = self.model.generate(
                    inputs,
                    max_length=inputs.shape[1] + max_tokens,
                    temperature=temperature,
                    do_sample=True
                )
                response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
                # Elimină promptul din răspuns
                return response[len(prompt):].strip()
            
        except Exception as e:
            return f"[ERROR] Eroare la generare: {str(e)}"
        
        return "[ERROR] Tip model necunoscut"


def create_real_llm(model_name: str, model_type: str = "auto", model_path: Optional[str] = None):
    """
    Factory function pentru crearea unui LLM real
    
    Args:
        model_name: Numele modelului (mistral, qwen, etc.)
        model_type: Tipul conexiunii (auto, llama_cpp, gpt4all, transformers)
        model_path: Calea către model (opțional)
    
    Returns:
        Instanță LLM conectată la model real
    """
    connector = LLMConnector(model_type=model_type, model_path=model_path)
    
    class RealLLM:
        def __init__(self, connector, name):
            self.connector = connector
            self.name = name
            self.model_type = connector.model_type
        
        def generate(self, prompt: str, max_tokens: int = 500) -> str:
            return self.connector.generate(prompt, max_tokens=max_tokens)
    
    return RealLLM(connector, model_name)
