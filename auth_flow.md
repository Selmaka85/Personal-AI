
# 🔐 ASTRA AUTH FLOW – Autentificare Completă 2FA / 3FA

---

## 🎯 OBIECTIV

Asigurarea accesului **exclusiv pentru Cătălin** la instanța Astra, prin browser (desktop / mobil), folosind autentificare strictă:

- 2FA obligatoriu (parolă + TOTP)
- 3FA opțional (parolă + TOTP + fingerprint device)
- Blocare automată la comportament suspect

---

## 🌐 SCENARIU DE ACCES – BROWSER

### 🔸 URL Acces:
```
https://astra.tau.local:4311
```

---

## 🛡️ FLUX DE AUTENTIFICARE

### 🔹 PAS 1 – Parolă (Nivel 1)
- Introducere parola principală
- Verificare bcrypt / argon2 hash
- Dacă e incorectă → blocare temporară după 3 încercări

### 🔹 PAS 2 – TOTP (Nivel 2)
- Se cere cod generat (30 sec.) de aplicația ta TOTP (Authy, Google Authenticator)
- Cod sincronizat cu secretul personal
- Dacă expiră → reîncercare

### 🔹 PAS 3 – Device Fingerprint (Nivel 3 – opțional)
- Sistemul verifică:
  - IP curent
  - MAC (dacă e disponibil)
  - User-Agent
  - Session token criptat
- Dacă e un device necunoscut:
  - Se cere confirmare Telegram sau cod fallback
  - Sau sistemul intră în lockdown pentru 15 minute

---

## ✅ DUPĂ AUTENTIFICARE
- Acces la UI complet:
  - Dashboard
  - Fișiere
  - Upload
  - Comenzi vocale / chat
  - Logs

---

## 🔒 MĂSURI DE SIGURANȚĂ

- 📵 3 încercări eșuate → ban IP + notificare Telegram
- 🕒 Timeout sesiune (ex: 15 min inactivitate)
- 📦 Toate requesturile sunt logate în `auth_log.json`
- 🔁 Device nou? Confirmare prin token + TOTP + delay

---

## 🔐 SECURITATE FIZICĂ

- Recomandare: adaugă YubiKey sau cod fizic scris de mână pentru layer 3
- Nu activa acces din Wi-Fi public sau IP necunoscut
- Configurează VPN în paralel (ex: Tailscale, WireGuard)

---

## 💬 CONCLUZIE

> Cu acest mecanism, nimeni altcineva nu poate intra.  
> Doar tu, cu cheia ta, cu codul tău, cu device-ul tău.

**Accesul la Astra e sacru. Nu se forțează. Nu se ghicește. Nu se fentează.**

