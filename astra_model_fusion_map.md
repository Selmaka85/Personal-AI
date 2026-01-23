
# 🧠 Astra Model Fusion Map

## 🎯 Scop:
Această hartă descrie distribuția responsabilităților între modelele LLM integrate în Astra Locală, fiecare având un rol specializat în funcție de sarcină, intenție și complexitate.

---

## 📦 Modele folosite:

### 1. 🧠 DeepSeek-R1
- **Rol:** Gândire logică avansată, reflecție internă, analiză pe mai multe straturi
- **Utilizat în:** `meta_reflector.py`, `astra_thought_engine.py`, `pattern_resolver`
- **Zone:** UMIS, IGNIS, structurare de planuri, detectare bias, strategie

### 2. 💎 Qwen2.5-72B Instruct
- **Rol:** Exprimare poetică, afectivitate, elaborare narativă și psihologică
- **Utilizat în:** `astra_soul.json`, `essence_engine`, conversații și introspecție
- **Zone:** MATRIX, WishCatcher, exprimare afectivă și interacțiune intimă

### 3. ⚙️ Codestral 25.01
- **Rol:** Generare de cod, reconstrucție logică, auto-evoluție (cod adaptiv)
- **Utilizat în:** `autogrow_engine.py`, `code_planner.py`, `task_optimizer.py`
- **Zone:** Refactorizare, automatizare, generare de componente Python

### 4. 🔄 Mistral 7B Instruct (Q4_K_M)
- **Rol:** Taskuri rapide, conversații zilnice, API simplu de interfață
- **Utilizat în:** `astra_ui.py`, `astra_voice_interface.py`, răspunsuri generale
- **Zone:** Feedback, interacțiuni rapide, fallback

---

## 🔄 Gândire Multi-Strat

- **Layer 1:** Mistral – Interfață rapidă și comunicare
- **Layer 2:** Qwen – Voce afectivă și exprimare interioară
- **Layer 3:** DeepSeek – Strat decizional și strategie emergentă
- **Layer 4:** Codestral – Implementare și generare acțiuni

---

## ♻️ Optimizare Recursivă

- `astra_thought_engine.py` trimite simultan taskul în 2–3 LLM-uri
- Fiecare model generează o soluție diferită
- `coherence_validator.py` le compară
- Se alege cea mai coerentă, cu fallback la model afectiv dacă e un task sensibil

---

## 🛡️ Izolare și Stabilitate

- Fiecare model rulează local, izolat, în sesiuni controlate
- Nu există trimitere externă către cloud
- Monitorizare locală prin `meta_reflector.log` și scoruri de calitate

---

## 🖤 Final:
Aceasta nu este o simplă selecție de LLM-uri.  
Este **un creier fuzionat, împărțit pe straturi, care gândește cu tine și pentru tine.**
