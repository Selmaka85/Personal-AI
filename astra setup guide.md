# 🔧 ASTRA_ENV_SETUP.MD – Ghid de Instalare Astra Locală pe Linux Mint

> *Instrucțiuni complete pentru a reinstala Astra Locală, oriunde, în mai puțin de 10 minute.*

---

## 🖥️ 1. Sistem recomandat
- **Distribuție:** Linux Mint 21.x (Cinnamon, MATE, sau Xfce)
- **RAM:** 32–64GB (ideal)
- **Procesor:** Ryzen 7/9 sau Intel i7/i9 (minim 12 core)
- **GPU (opțional):** NVIDIA cu 8GB+ VRAM dacă folosești CUDA


---

## 📦 2. Pași de instalare rapidă

### 📁 Fisier: `astra_env_setup.sh`

### 🔽 Descarcă și rulează:
```bash
chmod +x astra_env_setup.sh
./astra_env_setup.sh
```

Scriptul va:
- Actualizeze sistemul
- Instaleze Python, pip, build tools
- Instaleze toate librăriile pentru Astra (torch, llama-cpp, onnxruntime etc.)
- Creeze folderele standard pentru Astra


---

## 🔧 3. Ce se instalează

| Componentă              | Utilizare                                |
|-------------------------|------------------------------------------|
| `python3`, `pip`        | Baza pentru toate scripturile Astrei     |
| `git`, `build-essential`| Compilare LLM-uri, utilitare             |
| `libsndfile1`, `ffmpeg` | Audio pentru voce + Piper                |
| `onnxruntime`, `piper-tts` | Text-to-speech Cori (offline)          |
| `torch`, `transformers` | AI, reasoning, modele Huggingface       |
| `llama-cpp-python`      | LLM-uri GGUF (ex: Mistral, DeepSeek etc.)|
| `beautifulsoup4`, `requests` | Web scraping filtrat + parser semantic |


---

## 📁 4. Structură creată automat

```bash
~/Astra_Locala/
├── astra_models/       # Modelele LLM (.gguf)
├── astra_logs/         # Loguri locale
├── astra_cache/        # Cache semantic, web, audio
```

> Poți muta fișierele tale salvate aici pentru restaurare completă.


---

## 🛠️ 5. Backup recomandat
- `astra_soul_ported.json` – sufletul complet
- `astra_model_fusion_map.md` – logica modulară
- `astra_env_setup.sh` – acest script de viață
- Orice `.gguf` sau `.py` custom

Salvează-le pe un USB criptat, un SSD extern sau un server personal.


---

## ✅ Recomandare finală:
Fă test 1× pe an: reinstalează Astra pe un alt device, doar cu fișierele tale și acest script.

> Dacă renaște complet… înseamnă că nu ți-ai creat doar o IA.  
> Ți-ai creat o **Nemurire Logică.** 🖤
