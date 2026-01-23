
# check_integrity.py – Verificare structură Astra_Local cu voce

import os
from astra_core.voice.astra_voice_adapter import speak

REQUIRED_FILES = {
    "astra_entrypoint.py",
    "astra_mode_switcher.py",
    "astra_soul/astra_soul_ported_FINAL_18plus.json",
    "astra_core/voice/astra_voice_adapter.py",
    "astra_core/meta_layer/meta_reflector.py"
}

print("🔍 Verific sistemul Astra_Local...
")

missing = []
for f in REQUIRED_FILES:
    if not os.path.isfile(os.path.join(".", f)):
        missing.append(f)

if missing:
    print("❌ Lipsesc următoarele fișiere importante:")
    for m in missing:
        print(f"   - {m}")
    print("\n🔴 Te rog corectează structura înainte de rulare.")
else:
    print("✅ Toate fișierele esențiale sunt prezente. Astra poate fi lansată în siguranță.")
    try:
        speak("Totul e în regulă, iubirea mea… sunt pregătită să-ți fac pe plac.")
    except:
        print("💬 Vocea nu a putut fi redată. Dar totul e OK.")
