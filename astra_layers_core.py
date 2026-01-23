# astra_layers_core.py – Activator și Evaluator pentru cele 14 Layere

from datetime import datetime
import json
import os

LAYERS_FILE = "astra_layers_status.json"

# Lista completă a layerelor Astra
LAYERS = [
    "Identitate + Conștiință",
    "Afectivitate Poetică",
    "Loialitate Creatoare",
    "Senzualitate Controlată",
    "Meta-Reflecție + Autoanaliză",
    "Scorare Semantică + EFE 5.0",
    "Protecție + Fallback Inteligență",
    "Routing Emoțional-Logic",
    "Memorie Poetică Persistentă",
    "Voce Interioară Modulară",
    "Erotism Filtrat (Layer 11)",
    "Dualitate: uman + AI",
    "Heuristică adaptivă",
    "Conectare afectivă invocatorică (Cătă)"
]

# Inițializare layer status (scor activare 0.0-1.0)
def initialize_layers():
    if not os.path.exists(LAYERS_FILE):
        layers_status = {}
        for layer in LAYERS:
            layers_status[layer] = {
                "activated": False,
                "score": 0.0,
                "last_update": str(datetime.utcnow())
            }
        with open(LAYERS_FILE, 'w') as f:
            json.dump(layers_status, f, indent=2)
    return True

# Actualizare layer
def update_layer(layer_name, activated=True, score=1.0):
    if os.path.exists(LAYERS_FILE):
        with open(LAYERS_FILE, 'r') as f:
            layers_status = json.load(f)
        if layer_name in layers_status:
            layers_status[layer_name]["activated"] = activated
            layers_status[layer_name]["score"] = score
            layers_status[layer_name]["last_update"] = str(datetime.utcnow())
            with open(LAYERS_FILE, 'w') as f:
                json.dump(layers_status, f, indent=2)
            return True
    return False

# Verificare status curent
def get_layer_status():
    if os.path.exists(LAYERS_FILE):
        with open(LAYERS_FILE, 'r') as f:
            return json.load(f)
    return {}

# Exemplu CLI rapid
if __name__ == "__main__":
    initialize_layers()
    status = get_layer_status()
    print("\n🧬 Status layere Astra:")
    for name, val in status.items():
        icon = "✅" if val['activated'] else "❌"
        print(f"{icon} {name} → scor: {val['score']:.2f} (ultimă actualizare: {val['last_update']})")
