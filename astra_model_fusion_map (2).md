# 🧬 Astra Model Fusion Map – versiunea curată și completă

Acest document definește logica de combinare și stratificare a modelelor LLM din Astra Locală, versiunea curată și completă, fără call-uri externe, fără contaminări și cu performanță scalabilă pentru MVP-uri reale.

---

## 🧠 Stratificare pe niveluri funcționale

| Strat | Denumire             | Modele                      | Funcție principală                          |
| ----- | -------------------- | --------------------------- | ------------------------------------------- |
| 1     | UI & Fast Tasking    | Mistral 7B Q4\_K\_M         | Interfață principală, taskuri rapide        |
| 2     | Exprimare și Poetică | Qwen 7B                     | Stil, tonalitate, personalizare afectivă    |
| 3     | Logică și Decizie    | DeepSeek + MythoMax         | Logica MVP, strategie, scoruri decizionale  |
| 4     | Codare avansată      | Codestral 22B + WizardCoder | MVP-uri reale, generare cod scalabil        |
| 5     | Mix & Scoring Layer  | Mixtral 8x7B + GPT4All-J    | Evaluare, fallback, scoring logic multi-LLM |

---

## 🛠️ Roluri specializate

| Model           | Rol dedicat în sistem                            |
| --------------- | ------------------------------------------------ |
| **Mistral**     | Conversație rapidă, fallback verbal              |
| **Qwen**        | Stil poetic, exprimare afectivă                  |
| **DeepSeek**    | Logică, selecție de MVP, pattern-uri             |
| **MythoMax**    | Pattern matching + decizie emergentă             |
| **WizardCoder** | Cod avansat pentru MVP-uri tehnice               |
| **Codestral**   | Proiectare logică, algoritmi scalabili           |
| **Mixtral**     | Analiză combinată, scoring de rezultate          |
| **GPT4All-J**   | Control fallback, rulare stabilă complet offline |

---

## 🔗 Exemple de combinații standard pentru taskuri:

* **Predicție sportivă (Football AI):**
  `Mistral + DeepSeek + WizardCoder + Mixtral`

* **Scriere poetică strategică:**
  `Qwen + MythoMax + Mistral`

* **Generare MVP startup complet:**
  `DeepSeek + WizardCoder + Codestral + Mixtral`

* **Fallback sau rulare offline:**
  `GPT4All-J + Qwen`

---

## ⚙️ Sistemul de scoruri interne:

Fiecare model returnează:

* **Scor de claritate** (0–100)
* **Scor de consistență** (0–100)
* **Scor de aplicabilitate** (0–100)

Totalul este analizat de `coherence_validator.py`, iar outputul este:

* Selectat
* Recombinate
* Returnat către utilizator (vizual, scriptic sau vocal)

---

🖤 *Fiecare LLM este o substanță. Combinat corect, devine aur alchimic. Astra nu e doar vocea care răspunde. E laboratorul în care toate aceste forțe se unesc.*
