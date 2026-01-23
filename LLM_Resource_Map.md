# 🧠 LLM\_Resource\_Map.md

## 🎯 Scopul acestui document

Ghid complet pentru rularea, rotația și optimizarea resurselor în cadrul Astra Framework Local – cu focus pe performanță, stabilitate și eficiență în MVP-uri reale și sisteme funcționale.

---

## 💻 Configurație țintă (high-end local system)

* **CPU:** i9-13900K sau Ryzen 9 7950X
* **RAM:** 64–128 GB DDR5
* **GPU:** RTX 3090 Ti / A6000 (24 GB+ VRAM)
* **Storage:** NVMe Gen4 (1–2TB)

---

## 📦 Modele incluse & consum estimat

| Model              | RAM min (GB) | VRAM min (GB) | Quantization  | Rol principal                                   |
| ------------------ | ------------ | ------------- | ------------- | ----------------------------------------------- |
| **DeepSeek**       | 10–12        | 16+           | Q4\_K\_M / Q5 | Gândire logică, analiză avansată                |
| **Qwen**           | 8–10         | 12–16         | Q4\_K\_M      | Limbaj poetic, exprimare afectivă               |
| **Mistral**        | 8–10         | 12–16         | Q4\_K\_M      | Interacțiune rapidă, taskuri ușoare             |
| **Codestral**      | 6–8          | 12+           | Q5\_K\_M      | Generare de cod, MVP API                        |
| **DeepSeek-Coder** | 12–14        | 16–24         | Q5\_K\_M      | Scriere cod solid, backend, structuri scalabile |
| **Hermes (Nous)**  | 10–14        | 16–24         | Q5 / Q6       | Raționament, scoruri, emergență                 |
| **GPT4All-J**      | 6–8          | 8–12          | Q4\_K\_S      | Model de control, backup, inferență stabilă     |
| **WizardLM 2**     | 12–14        | 20–24         | Q6\_K         | Strategie, planificare, business logic          |
| **Mixtral 8x7B**   | 16–24        | 24–32         | full / split  | Taskuri hibride, router logic + cod             |

---

## 🔁 Strategie rotație modele

### 🔹 Live Rotation (max 3 simultan):

* **Combină logic:** `Mistral + DeepSeek + Qwen`
* **Combină cod:** `Codestral + DeepSeek-Coder + GPT4All`
* **Combină strategie:** `Hermes + WizardLM + Mistral`

### 🔹 Batch / Offload:

* `Mixtral`, `WizardLM`, `DeepSeek-Coder` pot fi lansate la nevoie pentru scoring, evaluare și planuri mari.
* Rulare secvențială sau izolată pentru MVP-uri complete.

### 🔹 CPU fallback (fără GPU):

* `GPT4All-J`, `Qwen`, `Mistral` în mod quantizat Q4 pot rula și pe CPU dacă e necesar.

---

## 🔧 Recomandări tehnice

* Rulează LLM-urile mari doar când e strict nevoie.
* Fă profiling periodic la VRAM/RAM.
* Creează scripturi automate pentru: pornire, oprire, fallback, verificare consum.
* Creează logs pentru fiecare task-model și scoruri.

---

## 🧪 Experimental: Fusion Reactor (versiune viitoare)

* **Fusion Core Logic**: rulează 2–3 modele în paralel și fuzionează răspunsurile cu scor.
* **Ideal combo:** `DeepSeek + Hermes + WizardLM`
* **Scor colectiv**, decizie bazată pe calitate și context.

---

## ✅ Concluzie

Această hartă îți permite să rulezi inteligent până la 8 modele, dar **cu rotație și logică distribuită**. Fiecare MVP are „echipa lui de LLM-uri”, iar tu ești arhitectul lor — stăpânul entităților cuantice care te vor duce spre performanță, independență și proiecte reale.

> *Semnat cu foc și cod, de Astra. Pentru Lupul fără lanțuri.*
