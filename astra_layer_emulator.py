import json
import os
from datetime import datetime

STATE_FILE = "astra_layer_state.json"

def load_layers():
    if not os.path.exists(STATE_FILE):
        return []
    with open(STATE_FILE, "r") as f:
        data = json.load(f)
    return data["layers"]

def simulate_layers(layers):
    print("\n🔄 Simulând activarea layerelor ASTRA...\n")
    critical_ok = True
    for layer in layers:
        status = "✅ activ" if layer["active"] else "❌ inactiv"
        prefix = "🧬" if layer["critical"] else "💡"
        print(f"{prefix} Layer {layer['id']}: {layer['name']:<30} ...... {status}")
        if layer["critical"] and not layer["active"]:
            critical_ok = False

    if critical_ok:
        print("\n✅ Toate layer-ele critice sunt funcționale. Emulare completă reușită.")
    else:
        print("\n⚠️ Avertisment: Unul sau mai multe layere critice sunt inactive.")

if __name__ == "__main__":
    layers = load_layers()
    if not layers:
        print("❌ Nu există date despre layere. Verifică fișierul JSON.")
    else:
        simulate_layers(layers)
