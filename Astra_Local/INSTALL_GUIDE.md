# 📦 ASTRA - Ghid de Instalare Completă

## 🚀 Instalare Rapidă (Minimal)

```bash
cd Astra_Local
python astra_entrypoint.py
```

Aceasta rulează ASTRA cu mock-uri funcționale.

## 🔧 Instalare Completă (Cu Funcționalități Reale)

### 1. Dependențe de Bază

```bash
pip install -r requirements_full.txt
```

### 2. Conectare Modele LLM Reale

#### Opțiunea A: Llama.cpp (Recomandat pentru local)

```bash
# Instalează llama-cpp-python
pip install llama-cpp-python

# Descarcă modele GGUF de la HuggingFace
# Exemplu: Mistral 7B
# https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF
```

Configurare:
```bash
# Setează variabile de mediu
export MISTRAL_MODEL_PATH="path/to/mistral-7b-instruct-v0.2.Q4_K_M.gguf"
export QWEN_MODEL_PATH="path/to/qwen-7b.Q4_K_M.gguf"
```

#### Opțiunea B: Ollama (Cel mai ușor)

```bash
# Instalează Ollama de la https://ollama.ai
# Apoi descarcă modele:
ollama pull mistral
ollama pull qwen
ollama pull deepseek
```

Configurare în `storage/configs/llm_config.json`:
```json
{
  "ollama": {
    "enabled": true,
    "base_url": "http://localhost:11434"
  }
}
```

#### Opțiunea C: OpenAI API

```bash
pip install openai
export OPENAI_API_KEY="your-api-key"
```

### 3. TTS (Text-to-Speech)

```bash
pip install piper-tts onnxruntime

# Descarcă vocea Cori
# https://github.com/rhasspy/piper/releases
```

Configurare:
```bash
export TTS_ENABLED="true"
export TTS_VOICE="cori"
export TTS_MODEL_PATH="path/to/cori-med.onnx"
```

### 4. Generare Imagini

```bash
pip install diffusers transformers accelerate torch pillow

# Necesită GPU cu 8GB+ VRAM pentru SDXL
# Sau folosește CPU (foarte lent)
```

Configurare:
```bash
export IMAGE_GEN_ENABLED="true"
export IMAGE_MODEL="stable-diffusion-xl"
export IMAGE_DEVICE="cuda"  # sau "cpu"
```

### 5. ML Predictor

```bash
pip install scikit-learn xgboost numpy pandas
```

### 6. Web UI

```bash
pip install flask flask-cors
```

## 📝 Configurare

### Fișier .env (opțional)

Creează `.env` în directorul `Astra_Local`:

```env
# LLM Models
MISTRAL_MODEL_PATH=path/to/mistral.gguf
QWEN_MODEL_PATH=path/to/qwen.gguf
DEEPSEEK_MODEL_PATH=path/to/deepseek.gguf

# OpenAI (opțional)
OPENAI_API_KEY=your-key-here

# TTS
TTS_ENABLED=true
TTS_VOICE=cori
TTS_MODEL_PATH=path/to/cori-med.onnx

# Image Generation
IMAGE_GEN_ENABLED=false
IMAGE_MODEL=stable-diffusion-xl
IMAGE_DEVICE=auto

# Ollama
OLLAMA_BASE_URL=http://localhost:11434
```

### Configurare Manuală

Editează `storage/configs/settings.json` pentru:
- Praguri EFE
- Modele preferate
- Setări UI

Editează `storage/configs/llm_config.json` pentru:
- Configurare modele LLM
- Activare/dezactivare modele

## 🎮 Utilizare

### Mod CLI

```bash
python astra_entrypoint_enhanced.py
```

### Mod Web UI

```bash
python astra_entrypoint_enhanced.py
# Apoi în interfață: tasta 'web'
```

Sau direct:
```bash
python user_interface/web_ui.py
```

## 🔍 Verificare Instalare

```bash
python test_astra.py
```

Toate testele ar trebui să treacă.

## ⚠️ Notă Importantă

- **Mock-urile funcționează fără instalări suplimentare**
- **Modelele reale necesită hardware adecvat** (GPU pentru imagini, RAM pentru LLM-uri)
- **Poți folosi ASTRA incremental** - activează funcționalitățile pe măsură ce le instalezi

## 🆘 Troubleshooting

### Eroare: "Module not found"
```bash
pip install -r requirements_full.txt
```

### Eroare: "CUDA out of memory"
- Folosește modele mai mici (Q4_K_M în loc de Q8)
- Sau folosește CPU (mai lent)

### Eroare: "Model path not found"
- Verifică variabilele de mediu
- Sau editează `storage/configs/llm_config.json`

---

**ASTRA** - *Sistem AI Local, Personalizat, Emergent*
