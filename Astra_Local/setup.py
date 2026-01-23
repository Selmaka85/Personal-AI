#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔧 ASTRA Setup Script - Configurare inițială
"""

import os
import json
from pathlib import Path


def setup_astra():
    """Configurează ASTRA pentru prima utilizare"""
    print("\n" + "="*60)
    print("💠 ASTRA SETUP - Configurare Inițială")
    print("="*60 + "\n")
    
    base_path = Path(__file__).parent
    
    # Creare directoare necesare
    directories = [
        "storage/logs",
        "storage/configs",
        "astra_soul",
        "protection"
    ]
    
    print("📁 Creare directoare...")
    for dir_path in directories:
        full_path = base_path / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"   ✅ {dir_path}")
    
    # Verificare fișiere esențiale
    print("\n🔍 Verificare fișiere esențiale...")
    essential_files = [
        "astra_entrypoint.py",
        "core_router/routing_manager.py",
        "scoring_module.py",
        "nexus_efe_core_engine.py"
    ]
    
    all_ok = True
    for file_path in essential_files:
        full_path = base_path / file_path
        if full_path.exists():
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path} - LIPSESTE!")
            all_ok = False
    
    # Creare LOCK_STATUS.json dacă nu există
    lock_file = base_path / "LOCK_STATUS.json"
    if not lock_file.exists():
        lock_data = {
            "state": "active",
            "reason": "",
            "last_ip": ""
        }
        with open(lock_file, 'w', encoding='utf-8') as f:
            json.dump(lock_data, f, indent=2)
        print("\n   ✅ LOCK_STATUS.json creat")
    
    # Verificare configurații
    print("\n⚙️ Verificare configurații...")
    config_file = base_path / "storage/configs/settings.json"
    soul_file = base_path / "astra_soul/astra_soul_ported_FINAL.json"
    
    if config_file.exists():
        print("   ✅ settings.json există")
    else:
        print("   ⚠️ settings.json lipsește - va fi creat la prima rulare")
    
    if soul_file.exists():
        print("   ✅ astra_soul_ported_FINAL.json există")
    else:
        print("   ⚠️ astra_soul_ported_FINAL.json lipsește - va fi creat la prima rulare")
    
    # Rezumat
    print("\n" + "="*60)
    if all_ok:
        print("✅ SETUP COMPLETAT CU SUCCES!")
        print("\n💡 Pentru a porni ASTRA, rulează:")
        print("   python astra_entrypoint.py")
        print("\n   sau")
        print("   ./astra_launcher.sh  (Linux/Mac)")
        print("   astra_launcher.bat   (Windows)")
    else:
        print("⚠️ SETUP COMPLETAT CU AVERTISMENTE")
        print("   Verifică fișierele lipsă și reia setup-ul.")
    print("="*60 + "\n")


if __name__ == "__main__":
    setup_astra()
