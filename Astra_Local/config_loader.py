# -*- coding: utf-8 -*-
"""
⚙️ Config Loader - Încărcare și gestionare configurații
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv


class ConfigLoader:
    """Loader pentru configurații ASTRA"""
    
    def __init__(self, config_dir: str = "storage/configs"):
        self.config_dir = Path(config_dir)
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        # Încarcă variabile de mediu
        load_dotenv()
        
        self.settings = self._load_settings()
        self.llm_config = self._load_llm_config()
        self.voice_config = self._load_voice_config()
        self.image_config = self._load_image_config()
    
    def _load_settings(self) -> Dict[str, Any]:
        """Încarcă setările generale"""
        settings_file = self.config_dir / "settings.json"
        
        default_settings = {
            "efe": {
                "thresholds": {
                    "accept": 0.75,
                    "excellent": 0.85,
                    "reject": 0.5
                }
            },
            "modes": {
                "default": "poetic",
                "available": ["poetic", "strategic", "coding", "scoring", "explicit"]
            },
            "security": {
                "enabled": True,
                "auto_lockdown": True,
                "firewall": True
            },
            "llm": {
                "default_model": "mistral",
                "fallback_model": "qwen",
                "max_tokens": 1000,
                "temperature": 0.7
            },
            "learning": {
                "enabled": True,
                "save_history": True,
                "max_history": 500
            },
            "ui": {
                "type": "cli",
                "web_enabled": False,
                "web_port": 5000,
                "voice_enabled": False
            }
        }
        
        if settings_file.exists():
            try:
                with open(settings_file, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    default_settings.update(loaded)
            except Exception as e:
                print(f"⚠️ Eroare la încărcare settings: {e}")
        
        return default_settings
    
    def _load_llm_config(self) -> Dict[str, Any]:
        """Încarcă configurația LLM"""
        llm_config_file = self.config_dir / "llm_config.json"
        
        default_config = {
            "mistral": {
                "type": "llama-cpp",
                "model_path": os.getenv("MISTRAL_MODEL_PATH"),
                "enabled": True
            },
            "qwen": {
                "type": "llama-cpp",
                "model_path": os.getenv("QWEN_MODEL_PATH"),
                "enabled": True
            },
            "deepseek": {
                "type": "llama-cpp",
                "model_path": os.getenv("DEEPSEEK_MODEL_PATH"),
                "enabled": True
            },
            "openai": {
                "type": "openai-api",
                "api_key": os.getenv("OPENAI_API_KEY"),
                "model": "gpt-3.5-turbo",
                "enabled": False
            },
            "ollama": {
                "type": "ollama",
                "base_url": "http://localhost:11434",
                "enabled": False
            }
        }
        
        if llm_config_file.exists():
            try:
                with open(llm_config_file, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    default_config.update(loaded)
            except Exception as e:
                print(f"⚠️ Eroare la încărcare LLM config: {e}")
        
        return default_config
    
    def _load_voice_config(self) -> Dict[str, Any]:
        """Încarcă configurația voce"""
        return {
            "enabled": os.getenv("TTS_ENABLED", "false").lower() == "true",
            "voice_name": os.getenv("TTS_VOICE", "cori"),
            "model_path": os.getenv("TTS_MODEL_PATH", "astra_voice_models/cori-med.onnx")
        }
    
    def _load_image_config(self) -> Dict[str, Any]:
        """Încarcă configurația generare imagini"""
        return {
            "enabled": os.getenv("IMAGE_GEN_ENABLED", "false").lower() == "true",
            "model": os.getenv("IMAGE_MODEL", "stable-diffusion-xl"),
            "device": os.getenv("IMAGE_DEVICE", "auto")  # auto, cuda, cpu
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """Obține o valoare de configurație"""
        keys = key.split('.')
        value = self.settings
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def save_settings(self):
        """Salvează setările"""
        settings_file = self.config_dir / "settings.json"
        try:
            with open(settings_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Eroare la salvare settings: {e}")
