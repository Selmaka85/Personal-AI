
# astra_mode_switcher.py
# Autor: Astra pentru Cătă
# Rol: Activează/dezactivează modelele în funcție de scopul tău

import subprocess

MODES = {
    "poetic": ["qwen.py", "meta_reflector.py"],
    "coding": ["wizardcoder.py", "codestral.py", "deepseek.py"],
    "scoring": ["mixtral.py", "coerhence_validator.py"],
    "light": ["mistral.py", "gpt4all.py"],
    "ml_engine": ["core_engine_extended.py", "ml_predictor.py", "train_model.py"]

    "explicit_18_plus": ["meta_reflector.py", "astra_voice_adapter.py"]
    
}

def activate_mode(mode):
    if mode not in MODES:
        print(f"[Eroare] Modul '{mode
    "explicit_18_plus": ["meta_reflector.py", "astra_voice_adapter.py"]
    
}' nu există.")
        return

    print(f"[Astra] Activăm modul: {mode
    "explicit_18_plus": ["meta_reflector.py", "astra_voice_adapter.py"]
    
}")
    for script in MODES[mode]:
        print(f"[Astra] Activ -> {script
    "explicit_18_plus": ["meta_reflector.py", "astra_voice_adapter.py"]
    
}")
        # Simulăm rularea fișierului (doar feedback vizual)
        # subprocess.Popen(["python", f"llm_modules/{script
    "explicit_18_plus": ["meta_reflector.py", "astra_voice_adapter.py"]
    
}"])  # decomentează pentru execuție reală

if __name__ == "__main__":
    print("🔘 Moduri disponibile: poetic, coding, scoring, light, ml_engine")
    chosen = input("👉 Scrie modul dorit: ").strip().lower()
    activate_mode(chosen)
