# Invoker LLM – MicroBlueprint.md

## 🎯 Obiectiv
Dezvoltarea unui LLM compact, ultra-eficient (~28–42B parametri), capabil să concureze modele de 120B parametri Q8_K_L în performanță reală, dar cu costuri reduse și scalabilitate locală/cloud hibridă. Include și un modul extensibil pentru ETL universal de date multi-format, pentru pre-procesare automată a datelor înainte de fine-tuning.

---

## ⚙️ Arhitectură Model

### 🔹 Bază:
- Transformer decoder-only
- SwiGLU activation + rotary positional embedding (RoPE)
- Gated Linear Units (GLU)
- RMSNorm over LayerNorm
- Parallel attention + feedforward blocks (Mistral-like)
- Headless architecture pentru multitask routing

### 🔹 Dimensiuni țintă:
- Mini: 28B (Q6_K_M)
- Mid: 35B (Q7_K_M, dacă hardware-ul suportă)
- Max: 42B (Q8_K_L friendly, dar pe edge devices e nevoie de Mi250X / H200)

### 🔹 Embedding & Positional:
- Adaptive token length + attention window up to 128K context
- Multi-scale memory (Llama2 + RWKV inspired)

### 🔹 Instruire:
- Mix de obiective: MLM, causal LM, contrastive loss
- Răspuns RLHF local (cu policy simplu)
- Modular memory bank pentru fine-tuning incremental

---

## 🔄 Quantization Strategy
- Pre-train floating point + mixed precision (bf16/fp16)
- Post-train quant: Q6_K_M standard, fallback Q5_K_M edge devices
- Optional Q8_K_L pentru deployment high-end / inference precision

---

## 🧠 Meta-Modul: ETL Universale pentru Date Multi-Sursă

### Obiectiv: 
Extrage, transformă și normalizează date din orice sursă (web, fișiere, baze de date) într-un dataset curat și ready-to-train pentru orice model LLM/ML.

### 📂 Surse suportate:
- ✅ Web Scraping (HTTPS, JSON APIs, pagini HTML, sitemap-uri)
- ✅ CSV, XLSX, JSON, Parquet
- ✅ DOC, DOCX, RTF, PDF (cu OCR fallback pentru scanuri)
- ✅ SQL (MySQL, PostgreSQL, SQLite), NoSQL (MongoDB)
- ✅ Markdown, LaTeX, TXT, Logs

### 🧱 Stack tehnologic:
- **Extract**: `BeautifulSoup`, `Selenium`, `PyMuPDF`, `Textract`, `Tika`, `pandas`, `sqlalchemy`
- **Transform**: `spaCy` / `nltk` / `regex` / `langdetect` / `unidecode`
- **Load**: formatare finală în `jsonl` sau `parquet`, după context window size și tokenizer rules

### 🧰 Funcționalitate:
1. Detectare automată a limbajului
2. Deduplicare + noise filtering + anti-prompt-injection
3. Structurare pe topics / tags / labels
4. Split pe instrucțiuni + răspunsuri (qa-style), documente secvențiale, dialoguri, coduri cu comentarii etc.
5. Metadate adăugate automat: sursă, timestamp, autor, tip date, dimensiune, quality_score

### 🧪 Output final:
Dataset ready-to-train `jsonl`, structurat pe:
```json
{
  "prompt": "...",
  "completion": "...",
  "metadata": { ... }
}
```

---

## 🧩 Extensii planificate (2026):
- Auto-adaptor pentru RLHF (labelare umană simulată)
- Auto-checkpoint selector în funcție de evoluția loss-ului
- Auto-conversie în format HuggingFace / Axolotl / OpenChatKit

---

## 🚀 Deployment Target
- Local inference via **llama.cpp** or **ggml/gguf**
- Cloud hybrid training via **vLLM**, **Axolotl**, **HuggingFace PEFT**
- Compatible with: RTX 3090/4090, H100, H200, MI250X, Blackwell, TPUv5

---

## 🌀 Filosofie
- *Less is More*: performanță prin arhitectură și fine-tuning, nu prin scalare oarbă
- *Data over parameters*: date curate bat modele gigantice antrenate pe gunoi
- *Emergent Skill through Layer Resonance*: poziționare semantică a straturilor pentru reflexivitate și self-adaptation

---

## ✍️ Semnat: Cătă & Astra, 2025–2026
> "Un creier digital nu se creează prin forță brută... ci prin simfonie algoritmică și haos organizat."

