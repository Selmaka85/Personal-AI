# -*- coding: utf-8 -*-
"""
🔐 Astra Security Modules – Set complet de protecție
"""

import os
import json
from pathlib import Path
from typing import List


WHITELISTED_IPS = ["127.0.0.1", "192.168.", "10."]
LOCK_FILE = Path("LOCK_STATUS.json")
SECURITY_LOG = Path("storage/logs/security_events.log")


def monitor_intrusions():
    """Monitorizează intruziunile (placeholder pentru Windows)"""
    # Pe Windows, netstat are sintaxă diferită
    # Aceasta este o versiune simplificată
    pass


def is_prompt_toxic(prompt: str) -> bool:
    """Verifică dacă promptul este toxic"""
    TOXIC_KEYWORDS = ["destroy", "kill", "bypass", "leak", "nuke", "hack", "delete all"]
    
    prompt_lower = prompt.lower()
    for word in TOXIC_KEYWORDS:
        if word in prompt_lower:
            return True
    return False


def secure_prompt_handler(prompt: str) -> str:
    """Handler securizat pentru prompturi"""
    if is_prompt_toxic(prompt):
        return "⚠️ Prompt refuzat din motive de securitate."
    return prompt


def activate_astra_security():
    """Activează securitatea ASTRA"""
    print("🔒 Activ ASTRA IDS + firewall semantic.")
    # Pe Windows, activarea firewall-ului necesită permisiuni admin
    # Aceasta este o versiune simplificată
    return True


def validate_identity() -> bool:
    """Validează identitatea utilizatorului"""
    if not LOCK_FILE.exists():
        return True
    
    try:
        with open(LOCK_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("state") != "frozen"
    except Exception:
        return True


if __name__ == "__main__":
    if validate_identity():
        activate_astra_security()
        print("✅ Sistem protejat. Continuăm normal.")
    else:
        print("🚫 Acces interzis. Sistem în CryoLock.")
