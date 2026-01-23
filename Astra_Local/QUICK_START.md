# 🚀 ASTRA - Quick Start Guide

## Instalare Rapidă

### 1. Verificare Cerințe
- Python 3.8+ instalat
- 8GB+ RAM (recomandat 16GB+)

### 2. Setup Inițial

```bash
# Navighează la directorul ASTRA
cd Astra_Local

# Rulează setup (opțional - creează directoare necesare)
python setup.py

# SAU rulează direct ASTRA
python astra_entrypoint.py
```

### 3. Prima Rulare

La prima rulare, ASTRA va:
- ✅ Crea directoarele necesare
- ✅ Încărca configurațiile
- ✅ Verifica sistemul
- ✅ Porni modul interactiv

## Utilizare de Bază

### Comenzi Disponibile

```
Tu 🧑: [orice întrebare sau comandă]
✨ ASTRA: [răspuns generat]

Comenzi speciale:
- exit / quit    → Ieșire
- status         → Status sistem
- mode <nume>    → Schimbă modul
- help           → Ajutor
```

### Exemple

```
Tu 🧑: Scrie-mi o poezie
✨ ASTRA: [poezie generată]

Tu 🧑: Fă-mi un plan de MVP
✨ ASTRA: [plan generat]

Tu 🧑: Explică-mi cum funcționează ASTRA
✨ ASTRA: [explicație]
```

## Configurare

### Personalizare Personalitate

Editează: `astra_soul/astra_soul_ported_FINAL.json`

```json
{
  "personality": {
    "tone": "poetic-affective-strategic",
    "emotional_depth": 0.9
  }
}
```

### Configurare Sistem

Editează: `storage/configs/settings.json`

```json
{
  "efe": {
    "thresholds": {
      "accept": 0.75
    }
  },
  "modes": {
    "default": "poetic"
  }
}
```

## Conectare Modele LLM Reale

Modulele LLM sunt mock-uri funcționale. Pentru utilizare reală:

1. **Deschide** fișierul din `llm_modules/` (ex: `mistral.py`)
2. **Modifică** metoda `generate()` pentru a apela modelul tău real
3. **Exemplu**:

```python
def generate(self, prompt: str, max_tokens: int = 500) -> str:
    # Conectare la model real (ex: llama-cpp-python)
    from llama_cpp import Llama
    llm = Llama(model_path="path/to/model.gguf")
    response = llm(prompt, max_tokens=max_tokens)
    return response['choices'][0]['text']
```

## Structură Fișiere

```
Astra_Local/
├── astra_entrypoint.py       # 🎯 START AICI
├── core_router/              # Routing inteligent
├── llm_modules/              # Modele LLM
├── meta_layer/               # Meta-analiză
├── astra_core/engine/        # Motoare core
├── protection/               # Securitate
├── storage/                 # Config & logs
└── astra_soul/              # Personalitate
```

## Troubleshooting

### Eroare: "Module not found"
```bash
# Asigură-te că ești în directorul corect
cd Astra_Local
python astra_entrypoint.py
```

### Eroare: "File not found"
```bash
# Rulează setup
python setup.py
```

### Răspunsuri mock
- Modulele LLM sunt mock-uri pentru demonstrație
- Conectează-te la modele reale pentru răspunsuri reale

## Suport

- Verifică log-urile în `storage/logs/`
- Verifică configurațiile în `storage/configs/`
- Verifică personalitatea în `astra_soul/`

---

**ASTRA** - *Sistem AI Local, Personalizat, Emergent*
