# 🧠 Astra Framework Overview

**Scop:**
Această arhitectură reprezintă un **framework modular** pentru explorarea, combinarea și generarea de soluții din modelele LLM existente și suplimentare, cu scopul de a crea răspunsuri inovative, strategice și personalizate.

---

## 📦 Modele utilizate:

### 🔹 **Standard (Inițiale):**

* **DeepSeek** – Gândire logică avansată, analiză multi-strat.
* **Qwen** – Exprimare poetică și afectivitate.
* **Mistral** – Taskuri rapide, interacțiune de bază.
* **Codestral** – Generare de cod și reconstrucție logică.

### 🔹 **Extinse (Extra pentru plus valoare reală):**

* **DeepSeek-Coder** – Scriere de cod curat, structuri complexe, back-end.
* **Nous-Hermes 2 / OpenHermes 2.5** – Raționament, interpretări abstracte, emergență semantică.
* **GPT4All-J (Groovy v1.3)** – Stabilitate, inferență offline, bun ca model de control.
* **Mixtral 8x7B** – Putere compusă, scoruri ridicate în taskuri mixte.
* **WizardLM 2** – Instrucțiuni complexe, planificare strategică, business logic.

---

## 🔧 Structura Framework-ului:

### 1. **Input Handler:**

* Preia și analizează cerințele de la utilizator.
* Generare de input tematic pentru modele.

### 2. **Model Router:**

* Alege și combină modelele în funcție de cerințele taskului.
* Rulează logică de rotație și selecție în funcție de task/resource usage.

### 3. **Pattern Detection:**

* Detectează pattern-uri și soluții recurente în datele generate.

### 4. **Model Modules:**

* Fiecare LLM este un modul independent ce poate fi activat, modificat sau completat.
* Exemple:

  * `deepseek.py` – Gândire logică
  * `qwen.py` – Exprimare poetică
  * `mistral.py` – Taskuri rapide
  * `codestral.py` – Generare cod
  * `deepseekcoder.py` – Codare avansată
  * `hermes.py` – Raționamente și scoruri
  * `wizard.py` – Strategie și planificare
  * `mixtral.py` – Taskuri hibride

### 5. **Output Optimizer:**

* Optimizează soluțiile oferite de combinațiile LLM.
* Aplică scoruri comparative între outputuri generate de mai multe modele.

### 6. **Feedback System:**

* Monitorizează și învață din interacțiunile anterioare.
* Îmbunătățește continuu performanța framework-ului prin analiză de scoruri și succes MVP.

### 7. **LLM Resource Map (modul nou):**

* Ghidează ce modele sunt active, în ce mod (CPU/GPU), cu ce resurse, când trebuie rotație.
* Optimizează rularea pentru sistemele locale de tip high-end (64–128GB RAM, GPU 3090+/A6000).

---

## 🚀 Funcționare în practică:

* **Input tematic:** Utilizatorul definește cerințele (ex: „strategie marketing pentru startup”).
* **Model Routing:** Model Router selectează modelele potrivite și controlează execuția.
* **Output Scoring:** Framework-ul generează rezultate, le compară, și le livrează cu ratinguri de încredere.

---

## 💡 Cum să folosești acest framework:

* **Deschide taskuri specifice:** Testează combinații de modele pe teme concrete (ex: strategie financiară, MVP, cod generator).
* **Personalizează:** Adaptează inputurile și modelele în funcție de scopul tău.
* **Iterează:** Framework-ul învață și se ajustează continuu.

---

## 📆 Următorii pași:

* Implementarea unui prototip stabil.
* Testarea rotației între LLM-uri.
* Optimizarea consumului de resurse locale.
* Evaluare prin scoruri și MVP-uri reale.
