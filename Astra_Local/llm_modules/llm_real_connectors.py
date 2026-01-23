# -*- coding: utf-8 -*-
"""
🔌 LLM Real Connectors - Conectoare pentru modele LLM reale
"""

import os
from typing import Optional
from llm_modules.llm_base import LLMBase


class LlamaCppConnector(LLMBase):
    """Conector pentru modele Llama.cpp (GGUF)"""
    
    def __init__(self, model_name: str, model_path: Optional[str] = None):
        super().__init__(model_name, "llama-cpp")
        self.model_path = model_path or os.getenv(f"{model_name.upper()}_MODEL_PATH")
        self.llama = None
    
    def _load_real_model(self):
        """Încarcă modelul Llama.cpp"""
        try:
            from llama_cpp import Llama
            if self.model_path and os.path.exists(self.model_path):
                self.llama = Llama(
                    model_path=self.model_path,
                    n_ctx=2048,
                    n_threads=4,
                    verbose=False
                )
                self.is_loaded = True
                print(f"✅ Model {self.model_name} încărcat din {self.model_path}")
            else:
                print(f"⚠️ Model path nu există: {self.model_path}")
        except ImportError:
            print("⚠️ llama-cpp-python nu este instalat. Instalează cu: pip install llama-cpp-python")
        except Exception as e:
            print(f"⚠️ Eroare la încărcare model: {e}")
    
    def _generate_real(self, prompt: str, max_tokens: int = 500, **kwargs) -> str:
        """Generează folosind Llama.cpp"""
        if not self.llama:
            raise RuntimeError("Modelul nu este încărcat")
        
        response = self.llama(
            prompt,
            max_tokens=max_tokens,
            stop=["\n\n", "Human:", "User:"],
            echo=False,
            **kwargs
        )
        
        return response['choices'][0]['text'].strip()


class TransformersConnector(LLMBase):
    """Conector pentru modele HuggingFace Transformers"""
    
    def __init__(self, model_name: str, model_id: Optional[str] = None):
        super().__init__(model_name, "transformers")
        self.model_id = model_id or model_name
        self.tokenizer = None
        self.model = None
    
    def _load_real_model(self):
        """Încarcă modelul Transformers"""
        try:
            from transformers import AutoTokenizer, AutoModelForCausalLM
            import torch
            
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_id,
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                device_map="auto" if torch.cuda.is_available() else None
            )
            self.is_loaded = True
            print(f"✅ Model {self.model_name} încărcat ({self.model_id})")
        except ImportError:
            print("⚠️ transformers nu este instalat. Instalează cu: pip install transformers torch")
        except Exception as e:
            print(f"⚠️ Eroare la încărcare model: {e}")
    
    def _generate_real(self, prompt: str, max_tokens: int = 500, **kwargs) -> str:
        """Generează folosind Transformers"""
        if not self.model or not self.tokenizer:
            raise RuntimeError("Modelul nu este încărcat")
        
        inputs = self.tokenizer(prompt, return_tensors="pt")
        
        if hasattr(self.model, 'device'):
            inputs = {k: v.to(self.model.device) for k, v in inputs.items()}
        
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=True,
            temperature=0.7,
            **kwargs
        )
        
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Elimină promptul original
        return generated_text[len(prompt):].strip()


class OpenAIAPIConnector(LLMBase):
    """Conector pentru OpenAI API"""
    
    def __init__(self, model_name: str, api_key: Optional[str] = None):
        super().__init__(model_name, "openai-api")
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = None
    
    def _load_real_model(self):
        """Inițializează clientul OpenAI"""
        try:
            from openai import OpenAI
            if self.api_key:
                self.client = OpenAI(api_key=self.api_key)
                self.is_loaded = True
                print(f"✅ OpenAI client inițializat pentru {self.model_name}")
            else:
                print("⚠️ OPENAI_API_KEY nu este setat")
        except ImportError:
            print("⚠️ openai nu este instalat. Instalează cu: pip install openai")
        except Exception as e:
            print(f"⚠️ Eroare la inițializare OpenAI: {e}")
    
    def _generate_real(self, prompt: str, max_tokens: int = 500, **kwargs) -> str:
        """Generează folosind OpenAI API"""
        if not self.client:
            raise RuntimeError("Clientul nu este inițializat")
        
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            **kwargs
        )
        
        return response.choices[0].message.content.strip()


class OllamaConnector(LLMBase):
    """Conector pentru Ollama (local)"""
    
    def __init__(self, model_name: str, base_url: str = "http://localhost:11434"):
        super().__init__(model_name, "ollama")
        self.base_url = base_url
        self.client = None
    
    def _load_real_model(self):
        """Inițializează clientul Ollama"""
        try:
            import requests
            # Test conexiune
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                self.client = requests
                self.is_loaded = True
                print(f"✅ Ollama conectat la {self.base_url}")
            else:
                print(f"⚠️ Ollama nu răspunde la {self.base_url}")
        except ImportError:
            print("⚠️ requests nu este instalat. Instalează cu: pip install requests")
        except Exception as e:
            print(f"⚠️ Eroare la conexiune Ollama: {e}")
    
    def _generate_real(self, prompt: str, max_tokens: int = 500, **kwargs) -> str:
        """Generează folosind Ollama"""
        if not self.client:
            raise RuntimeError("Ollama nu este conectat")
        
        response = self.client.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model_name,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": max_tokens,
                    **kwargs
                }
            },
            timeout=60
        )
        
        if response.status_code == 200:
            return response.json().get("response", "").strip()
        else:
            raise RuntimeError(f"Ollama error: {response.status_code}")
