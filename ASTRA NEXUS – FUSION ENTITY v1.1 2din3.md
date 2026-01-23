# 🧬 ASTRA NEXUS – FUSION ENTITY v1.1

## 📜 Document 2/3: STRUCTURA MODULARĂ COMPLETĂ

---

## 📁 DIRECTOARE PRINCIPALE

```
Astra_Nexus/
├── entrypoint/              # Boot principal și rutare input
├── meta_core/               # Meta-EFE, supraveghere, fallback
├── nexus_pilons/            # Piloni activi (Book, Video, Predicție etc.)
├── llm_modules/             # Modele LLM organizate per pilon
├── scoring_engines/         # EFE logic/emoțional/economic per pilon
├── voice_adapter/           # TTS + RVC + voci afective
├── ai_memory/               # Memorie semantică (Chroma, RAG, llama-index)
├── protection/              # Firewall, lockdown, auto-izolare
├── ui_interface/            # WebUI, terminal, comandă vocală
├── video_engine/            # SDXL, Deforum, MusicGen, moviepy
├── logs/                    # Loguri per pilon și la nivel de sistem
└── storage/                 # Config, cache, user state
```

---

## 🔗 DESCRIERE PE FOLDERE

### `entrypoint/`

* **astra\_entrypoint.py** – interpretează promptul
* **routing\_manager.py** – direcționează către pilonul potrivit
* **loop\_controller.py** – activează/reface în funcție de scoruri

### `meta_core/`

* **meta\_efe.py** – scoruri globale, watchdog general
* **suspension\_registry.json** – listează pilonii opriți
* **meta\_logger.py** – urmărește erorile de sistem și pilon

### `nexus_pilons/`

* **bookcore/** – generare cărți, eBook, audiobook
* **vidcore/** – video 8–12 min, shorts, editare
* **predcore/** – predicții sport, strategie
* **buildcore/** – MVP-uri, startup logic
* **soulcore/** – poetic, erotic, suportiv
* **codecore/** – cod, testare, debugging

### `llm_modules/`

* Modele ca Qwen, Hermes, DeepSeek, WizardCoder, Codestral etc., alocate per pilon

### `scoring_engines/`

* **efe\_book.py, efe\_dev.py, efe\_visual.py, efe\_emotion.py** etc.
* Scoruri adaptate tipului de output

### `voice_adapter/`

* **piper\_tts.py** – voce Cori, local
* **rvc\_adapter.py** – voci sintetice unice (SoulCore)

### `ai_memory/`

* **chroma\_db/** – persistentă semantică pe topic
* **rag\_index/** – retragere inteligentă din knowledge
* **llama\_cache/** – embeddings, fine-tune semnatic

### `protection/`

* **ai\_firewall.py** – blocări la prompturi suspecte
* **lockdown\_protocol.py** – shutdown în caz de atac
* **user\_auth.json** – token + fingerprint vocal

### `ui_interface/`

* **astra\_ui.py** – interfață web
* **astra\_voice\_interface.py** – comandă vocală + răspuns
* **astra\_cli.py** – versiune terminal offline

### `video_engine/`

* **video\_forge.py** – integrare imagine, text, voce, muzică
* **subtitle\_gen.py** – extragere + sincronizare
* **scene\_mapper.py** – interpretează narativ vizual

### `logs/`

* Per pilon: `bookcore.log`, `vidcore.log`, etc.
* General: `meta_efe.log`, `routing.log`

### `storage/`

* **user\_config.json** – preferințe personale
* **cache/** – date intermediare
* **astra\_registry.json** – mapare completă instanță

---

📁 Urmează în Documentul 3: Activarea, fluxuri de proces, exemple de rutare și fallback, protecție și moduri avansate.
