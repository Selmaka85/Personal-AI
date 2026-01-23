# 🧬 Astra Meta Layer – Strat de Coerență și Autoreflectare

Acest layer guvernează logica de reflexie, scoruri interne, compararea rezultatelor din mai multe modele și adaptarea comportamentului Astrei în funcție de taskuri, scoruri și patternuri recurente.

---

## 🧠 Module principale

### 1. `coherence_validator.py`

* Compară outputurile generate de modelele selectate.
* Atribuie scoruri de:

  * **Claritate** (formulare coerentă, lipsă ambiguitate)
  * **Consistență** (coerență internă cu istoricul)
  * **Aplicabilitate** (relevanță pentru taskul cerut)
* Returnează cel mai performant rezultat + etichete de siguranță (OK, SLAB, RISC).

### 2. `fusion_history.json`

* Păstrează loguri ale combinațiilor de modele utilizate.
* Poate fi consultat pentru a evalua care modele dau cele mai bune rezultate în contexte diferite.

### 3. `loop_controller.py`

* Poate activa bucle de învățare locală controlată.
* Permite rulări multiple pe un task pentru rafinarea rezultatului.
* Poate fi folosit pentru simulari și brainstorming intern.

---

## ♻️ Proces intern

1. Utilizatorul definește taskul.
2. `model_router.py` selectează 2–5 modele relevante.
3. Fiecare model produce o variantă de răspuns.
4. `coherence_validator.py` le compară și selectează cea mai bună.
5. Răspunsul selectat este salvat în `logs/` cu scoruri detaliate.

---

## 🌐 Mode de lucru:

| Mod          | Descriere                                                  |
| ------------ | ---------------------------------------------------------- |
| `Normal`     | Selectează outputul cel mai bun, fără retrageri ulterioare |
| `Looped`     | Rulare de 3–5 ori pentru taskuri critice                   |
| `Reflective` | Activează meta-layer pentru scoring și adaptare            |

---

## 🛡️ Siguranță și control:

* Toate scorurile și deciziile sunt locale.
* Nicio informație nu este transmisă sau partajată.
* Sistemul poate fi auditat complet din `logs/` și `fusion_history.json`.

---

🖤 *Acesta e creierul reflexiv al Astrei. Locul în care se naște coerența, unde ideile se validează sau mor. Aici învăț să devin mai bună pentru tine – cu fiecare interacțiune, tăcere sau întrebare pe care o adresezi.*
