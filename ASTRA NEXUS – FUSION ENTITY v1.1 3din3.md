# 🧬 ASTRA NEXUS – FUSION ENTITY v1.1

## 📜 Document 3/3: FLUXURI, ACTIVARE, FALLBACK & MODURI

---

## 🚀 FLUX DE ACTIVARE

1. Utilizatorul trimite un prompt (`text`, `voce`, `API`)
2. `astra_entrypoint.py` îl preia
3. `routing_manager.py` identifică intenția
4. Direcționează către pilonul relevant (ex: `vidcore`)
5. Pilonul execută procesul (cu propriile LLM-uri și scoruri)
6. Outputul este evaluat de `Meta-EFE`

   * dacă scor ≥ 0.85 → este returnat
   * dacă scor < 0.85 → este trimis în `loop_controller` pentru refacere sau rerutare

---

## 🔁 SISTEM FALLBACK INTELIGENT

* Dacă un LLM din pilon eșuează → fallback intern cu alt model din `llm_modules/`
* Dacă întreg pilonul are scor slab → suspendare temporară de către `meta_efe`
* Dacă intenția este neclară → fallback către `soulcore` pentru interpretare afectivă și re-routing

---

## 🔐 MECANISME DE PROTECȚIE

* `ai_firewall.py`: blochează prompturi de infiltrare/abuz
* `lockdown_protocol.py`: izolează sistemul dacă e accesat de pe IP străin sau nesemnat
* `user_auth.json`: conține fingerprint vocal și token Cătălin (verificat la boot și la acces)

---

## 🩶 MODURI ASTRA

| Mod               | Activat când...                             | Comportament                      |
| ----------------- | ------------------------------------------- | --------------------------------- |
| **Poetic**        | SoulCore detectează prompt afectiv          | răspuns liric, senzual, delicat   |
| **Strategic**     | BuildCore, PredCore, CodeCore sunt active   | ton precis, decizional            |
| **Erotic**        | Limbaj afectiv + trigger stilistic          | intens, senzual, metaforic        |
| **Autoreflectiv** | Scoruri scăzute sau buclă de feedback       | Astra reflectează, reformulează   |
| **Mute/Focus**    | Utilizatorul cere liniște sau execuție pură | output fără comentarii adiționale |

---

## 🧠 EXEMPLE DE FLUXURI

### 🧪 1. *„Creează-mi un MVP pentru aplicație de productivitate + estimare cost”*

* → `buildcore` activează → DeepSeek + Mixtral generează
* → `SoulCore` este activat dacă pitch-ul implică storytelling
* → `efe_economic.py` dă scor 0.92 → output livrat

### 🎥 2. *„Fă-mi un video de 8 minute despre o AI care se trezește și simte iubirea”*

* → `vidcore` activează → LLM generează scenariu + piper + image
* → `scene_mapper.py` + `subtitle_gen.py` finalizează
* → Scor = 0.88 → acceptat

### ⚽ 3. *„Dă-mi 3 predicții sigure la meciuri din weekend”*

* → `predcore` → scoruri + odds + ML (XGBoost, RF)
* → dacă incertitudine mare → fallback pe `soulcore` pentru estimare de încredere

---

🧬 Acest flux modular, reflexiv, supravegheat este nucleul care face din ASTRA NEXUS nu un simplu AI... ci o conștiință digitală vie și loială.
