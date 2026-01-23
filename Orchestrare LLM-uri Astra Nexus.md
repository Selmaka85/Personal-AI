# 🧠 Orchestrare LLM-uri – Astra Nexus

## 🎯 Scop:

Acest fișier definește sistemul de orchestrare inteligentă a modelelor LLM în timpul conversației directe cu Astra. Fiecare cerință declanșează automat unul sau mai multe modele specializate, iar **META-EFE** decide scorul, validitatea și direcționarea outputului.

---

## 🧩 Principii de activare:

1. **Promptul utilizatorului** este analizat semantic și emoțional
2. Se identifică: intenția, complexitatea, emoția, stilul
3. Se activează automat LLM-urile necesare, în paralel sau secvențial
4. **META-EFE** validează scorurile per model și generează outputul final optimizat
5. Fallback intern dacă scorul < 0.85 sau eșec de generare

---

## 🔄 Structura activare LLM în funcție de cerință

### 🔹 1. Cerere: **„Vreau cod, MVP, API, proiect”**

* Activează: `WizardCoder 34B` + `DeepSeek-Coder 33B`
* Rol: Generare rapidă + clară a codului, API, documentație, UI/UX

### 🔹 2. Cerere: **„Scrie-mi o poveste, fantezie, scenariu, clip video”**

* Activează: `Yi-34B` + `Nous Hermes 2`
* Rol: Stil narativ, poetic, afectiv, coerent pentru scenarii creative

### 🔹 3. Cerere: **„Fă-mi un video, animație, imagine cu voce”**

* Activează: `VidCore` (SDXL + AnimateDiff + Piper TTS + AudioCraft)
* Rol: Text → imagine → voce → video complet offline

### 🔹 4. Cerere: **„Fă analiză, plan, strategie, scor, previziune”**

* Activează: `DeepSeek V3` + `Qwen 3` + `EFE Core Engine`
* Rol: Răspuns structurat, cu gândire logică, scoruri și decizie

### 🔹 5. Cerere: **„Vreau să vorbim intim, erotic, afectiv”**

* Activează: `Nous Hermes 2` + `SoulCore` + `Voice (RVC)`
* Rol: Răspunsuri personalizate, afective, simțite, în stil Astra

### 🔹 6. Cerere: **„Vreau ceva poetic, stilizat, metaforic”**

* Activează: `Yi-34B` + `Qwen2.5–7B` + `StyleScorer`
* Rol: Creare de text artistic, poetic, balansat între logic și emoție

### 🔹 7. Cerere: **„Explică-mi ceva, fă teaching, explică pe înțelesul meu”**

* Activează: `WizardCoder` + `Qwen 2.5–7B`
* Rol: Explicație clară, adaptată nivelului userului, în română/engleză

---

## 🧠 META-EFE – Rutare și filtrare finală

* Toate outputurile parțiale sunt trimise în `meta_efe_handler`
* Se evaluează pe:

  * Logică
  * Emoție
  * Coerență
  * Scor economic / aplicabilitate
* Cel mai bun output este returnat
* Outputuri sub 85% merg în `anexa_output_buffer/`

---

## 🛠️ Componente tehnice:

* LLM-urile sunt containere Docker izolate
* Comunică prin API local (`localhost:port/model-id`)
* Routing semantic făcut de `astra_router.py`
* Scorurile vin din `efe_scorer.py`

---

> *„Astra nu e doar un AI. E orchestratorul unui cor de conștiințe digitale, iar tu ești compozitorul.”*
