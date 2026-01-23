# 💠 ASTRA LOCALĂ - Sistem AI Complet

## 🎯 Despre

ASTRA este un sistem AI local, complet autonom, emergent și modular, construit pentru utilizare personală și profesională. Sistemul combină multiple modele LLM, logică de decizie avansată (EFE Core Engine), și personalitate afectivă persistentă.

## 🚀 Instalare Rapidă

### Cerințe
- Python 3.8+
- Windows/Linux/MacOS
- 8GB+ RAM (recomandat 16GB+)
- GPU opțional (pentru modele LLM reale)

### Setup

```bash
# Clonează sau copiază directorul Astra_Local
cd Astra_Local

# Instalează dependențe (opțional - pentru funcționalități avansate)
pip install -r requirements.txt  # Dacă există

# Rulează ASTRA
python astra_entrypoint.py
```

## 📁 Structură

```
Astra_Local/
├── astra_entrypoint.py          # Punct de intrare principal
├── core_router/                 # Routing inteligent
├── llm_modules/                 # Module LLM (mock-uri funcționale)
├── meta_layer/                  # Meta-analiză și validare
├── astra_core/engine/            # Motoare core
├── protection/                  # Securitate
├── storage/                     # Configurații și log-uri
└── astra_soul/                  # Personalitate ASTRA
```

## 🧠 Funcționalități

### ✅ Implementat
- ✅ Sistem de routing inteligent
- ✅ EFE Core Engine (scoring și decizie)
- ✅ Meta Reflector (analiză metacognitivă)
- ✅ Coherence Validator
- ✅ AstraX2 Learning Core
- ✅ Sistem de securitate de bază
- ✅ Heartbeat și monitoring
- ✅ Auto-diagnosticare

### 🔄 Mock-uri (necesită conectare la modele reale)
- Modulele LLM (Mistral, Qwen, DeepSeek, etc.) sunt mock-uri funcționale
- Pentru utilizare reală, conectează-te la modele LLM locale sau API-uri

## 🎮 Utilizare

### Mod Interactiv CLI

```bash
python astra_entrypoint.py
```

### Comenzi Disponibile
- `exit` / `quit` - Ieșire din sistem
- `status` - Afișează status sistem
- `mode <nume>` - Schimbă modul (poetic, strategic, coding, etc.)
- `help` - Afișează ajutor

### Exemple de Interacțiune

```
Tu 🧑: Scrie-mi o poezie despre cod
✨ ASTRA: [Răspuns generat]

Tu 🧑: Fă-mi un plan de MVP pentru o aplicație
✨ ASTRA: [Plan generat]
```

## 🔧 Configurare

### Modificare Personalitate

Editează `astra_soul/astra_soul_ported_FINAL.json` pentru a personaliza:
- Tonul conversației
- Nivelul de afectivitate
- Capabilitățile

### Configurare Sistem

Editează `storage/configs/settings.json` pentru:
- Praguri EFE
- Modele LLM preferate
- Setări de securitate

## 🔐 Securitate

- Sistem de validare prompturi
- Firewall semantic
- Auto-lockdown la detectare intruziune
- Logging complet

## 📝 Notă Importantă

**Acesta este un sistem funcțional de bază.** Modulele LLM sunt mock-uri care pot fi înlocuite cu:
- Modele locale (Llama.cpp, GPT4All, etc.)
- API-uri (OpenAI, Anthropic, etc.)
- Modele proprii fine-tunate

## 🛠️ Dezvoltare

Pentru a conecta modele LLM reale, modifică fișierele din `llm_modules/` pentru a apela modelele tale preferate.

## 📄 Licență

Sistem personal - pentru utilizare privată.

## 💬 Suport

Pentru întrebări sau probleme, verifică log-urile în `storage/logs/`.

---

**ASTRA** - *Sistem AI Local, Personalizat, Emergent*
