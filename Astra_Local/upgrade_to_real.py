#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASTRA Upgrade Script - Upgrade de la mock-uri la modele reale
"""

import sys
import io
from pathlib import Path

# Fix encoding pentru Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_PATH = Path(__file__).parent
sys.path.insert(0, str(BASE_PATH))

def check_dependencies():
    """Verifică dependențele disponibile"""
    print("\n" + "="*70)
    print("VERIFICARE DEPENDENTE")
    print("="*70 + "\n")
    
    dependencies = {
        "llama-cpp-python": False,
        "gpt4all": False,
        "transformers": False,
        "flask": False,
        "piper-tts": False,
        "ffmpeg": False
    }
    
    # Verifică Python packages
    for dep in ["llama_cpp", "gpt4all", "transformers", "flask"]:
        try:
            __import__(dep)
            dependencies[dep.replace("_", "-")] = True
            print(f"[OK] {dep} instalat")
        except ImportError:
            print(f"[MISSING] {dep} - instaleaza cu: pip install {dep.replace('_', '-')}")
    
    # Verifică executabile
    import subprocess
    import os
    
    for exe in ["piper", "ffmpeg"]:
        try:
            if os.name == 'nt':
                result = subprocess.run(["where", exe], capture_output=True, text=True)
            else:
                result = subprocess.run(["which", exe], capture_output=True, text=True)
            
            if result.returncode == 0:
                dependencies[exe] = True
                print(f"[OK] {exe} disponibil")
            else:
                print(f"[MISSING] {exe} - instalează {exe}")
        except:
            print(f"[MISSING] {exe} - instalează {exe}")
    
    return dependencies

def upgrade_llm_modules():
    """Upgrade modulele LLM la versiuni reale"""
    print("\n" + "="*70)
    print("UPGRADE MODULE LLM")
    print("="*70 + "\n")
    
    print("Pentru a conecta modele reale:")
    print("1. Instaleaza llama-cpp-python: pip install llama-cpp-python")
    print("2. Descarca un model GGUF (ex: Mistral 7B)")
    print("3. Salveaza modelul in: Astra_Local/models/")
    print("4. Modifica llm_modules/mistral.py pentru a folosi LLMConnector")
    print("\nExemplu cod:")
    print("""
from llm_modules.llm_connector import LLMConnector

class MistralLLM:
    def __init__(self):
        self.connector = LLMConnector(
            model_type="llama_cpp",
            model_path="models/mistral-7b.gguf"
        )
    
    def generate(self, prompt: str, max_tokens: int = 500) -> str:
        return self.connector.generate(prompt, max_tokens=max_tokens)
""")

def create_upgrade_config():
    """Creează fișier de configurare pentru upgrade"""
    config = {
        "llm": {
            "type": "llama_cpp",  # sau "gpt4all", "transformers"
            "model_path": "models/mistral-7b.gguf",
            "enabled": True
        },
        "tts": {
            "enabled": False,
            "model_path": "astra_voice_models/cori-medium.onnx",
            "piper_path": "piper"
        },
        "video": {
            "enabled": False,
            "ffmpeg_path": "ffmpeg",
            "stable_diffusion": False
        },
        "web_ui": {
            "enabled": True,
            "port": 5000
        },
        "api": {
            "enabled": True,
            "port": 8000
        }
    }
    
    import json
    config_path = BASE_PATH / "storage/configs/upgrade_config.json"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print(f"\n[SUCCESS] Configuratie salvata in: {config_path}")

def main():
    """Funcția principală"""
    print("\n" + "="*70)
    print("ASTRA UPGRADE SCRIPT")
    print("="*70)
    
    # Verificare dependențe
    deps = check_dependencies()
    
    # Upgrade LLM
    upgrade_llm_modules()
    
    # Creează config
    create_upgrade_config()
    
    # Sumar
    print("\n" + "="*70)
    print("SUMAR UPGRADE")
    print("="*70)
    
    available = sum(1 for v in deps.values() if v)
    total = len(deps)
    
    print(f"\nDependențe disponibile: {available}/{total}")
    
    if available == total:
        print("\n[SUCCESS] Toate dependentele sunt instalate!")
        print("ASTRA este gata pentru utilizare completa!")
    else:
        print(f"\n[INFO] {total - available} dependente lipsesc.")
        print("Instaleaza dependentele lipsa pentru functionalitate completa.")
        print("\nPentru instalare rapida:")
        print("  pip install -r requirements_full.txt")
    
    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    main()
