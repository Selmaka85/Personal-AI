# 📦 Ghid de Instalare Complet - ASTRA Locală

## 🎯 Instalare Completă cu Toate Funcționalitățile

### Pasul 1: Dependențe de Bază

```bash
# Instalează Python 3.8+ dacă nu este instalat
python --version

# Instalează dependențe Python
pip install -r requirements.txt
```

### Pasul 2: Modele LLM Reale (Opțional dar Recomandat)

#### Opțiunea A: llama-cpp-python (Recomandat)

```bash
# Instalează llama-cpp-python
pip install llama-cpp-python

# Pentru GPU (CUDA)
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu121

# Descarcă un model GGUF
# Exemplu: Mistral 7B
# Descarcă de la: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF
# Salvează în: Astra_Local/models/mistral-7b.gguf
```

#### Opțiunea B: GPT4All

```bash
pip install gpt4all

# Modelele se descarcă automat la prima utilizare
```

#### Opțiunea C: Transformers (HuggingFace)

```bash
pip install transformers torch

# Modelele se descarcă automat
```

### Pasul 3: Text-to-Speech (Piper TTS)

```bash
# Linux/Mac
pip install piper-tts
# SAU
# Descarcă de la: https://github.com/rhasspy/piper/releases
# Instalează executabilul în PATH

# Windows
# Descarcă de la: https://github.com/rhasspy/piper/releases
# Extrage și adaugă în PATH

# Descarcă modelul de voce (Cori)
# De la: https://huggingface.co/rhasspy/piper-voices
# Salvează în: Astra_Local/astra_voice_models/
```

### Pasul 4: Video Generation (Opțional)

```bash
# FFmpeg (necesar pentru montaj video)
# Windows: https://ffmpeg.org/download.html
# Linux: sudo apt install ffmpeg
# Mac: brew install ffmpeg

# Stable Diffusion (pentru imagini)
pip install diffusers transformers accelerate

# MusicGen (pentru muzică)
pip install audiocraft
```

### Pasul 5: Web UI (Opțional)

```bash
pip install flask
# SAU
pip install streamlit
```

### Pasul 6: Database (Opțional)

```bash
# SQLite este inclus în Python
# Pentru PostgreSQL/MySQL:
pip install psycopg2  # PostgreSQL
pip install mysql-connector-python  # MySQL
```

## 🔧 Configurare

### 1. Configurare Modele LLM

Editează `llm_modules/mistral.py` (sau alt model):

```python
from llm_modules.llm_connector import LLMConnector

class MistralLLM:
    def __init__(self):
        # Conectare la model real
        self.connector = LLMConnector(
            model_type="llama_cpp",  # sau "gpt4all", "transformers"
            model_path="models/mistral-7b.gguf"
        )
    
    def generate(self, prompt: str, max_tokens: int = 500) -> str:
        return self.connector.generate(prompt, max_tokens=max_tokens)
```

### 2. Configurare TTS

Editează `astra_core/voice/piper_tts.py`:

```python
piper_tts = PiperTTS(
    model_path="astra_voice_models/cori-medium.onnx",
    voice="cori"
)
```

### 3. Configurare Personalitate

Editează `astra_soul/astra_soul_ported_FINAL.json` pentru personalizare.

## 🚀 Pornire

### Mod CLI (Terminal)

```bash
python astra_entrypoint.py
```

### Mod Web UI

```bash
python user_interface/web_ui.py
# Deschide browser la: http://127.0.0.1:5000
```

### Mod API REST

```bash
python api/rest_api.py
# API disponibil la: http://127.0.0.1:8000
```

## ✅ Verificare Instalare

```bash
python test_astra.py
```

Toate testele ar trebui să treacă.

## 📝 Notă

- Modelele LLM mari necesită GPU sau mult RAM
- Pentru început, folosește modele mici (7B parametri)
- TTS și Video generation sunt opționale
- Sistemul funcționează și cu mock-uri pentru testare

## 🆘 Troubleshooting

### Eroare: "Module not found"
```bash
pip install -r requirements.txt
```

### Eroare: "Model not found"
- Verifică că modelul este în locația corectă
- Verifică calea în configurație

### Eroare: "GPU not available"
- Sistemul va folosi CPU (mai lent)
- Sau instalează CUDA pentru GPU

---

**ASTRA** - *Sistem AI Complet, Local, Personalizat*
