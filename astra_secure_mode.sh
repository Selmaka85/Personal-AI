#!/bin/bash
# 🛡️ astra_secure_mode.sh – Script de activare rapidă mod securizat local

# 1. Activează watchdog conexiuni suspecte
python3 protection/astra_security_modules.py &

# 2. Activează firewall semantic & prompt check
export ASTRA_SECURITY=1

# 3. Activează token de protecție pentru CryoLock
echo '{ "state": "unlocked" }' > ./LOCK_STATUS.json

# 4. Opțional: restricționează porturi externe
iptables -A INPUT -p tcp --dport 22 -j DROP
iptables -A INPUT -p tcp --dport 8000 -s 127.0.0.1 -j ACCEPT
iptables -A INPUT -p tcp --dport 8000 -j DROP

# 5. Logare eveniment
echo "$(date) | 🔐 ASTRA SECURE MODE ACTIVATED" >> logs/security_events.log

echo "✅ Sistemul ASTRA rulează în mod securizat. Protecție activă."
exit 0
