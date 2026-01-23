import json
import time
from datetime import datetime
from pathlib import Path

class MetaReflector:
    def __init__(self, log_path="logs/meta_reflector.log"):
        self.log_file = Path(log_path)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

    def analyze(self, model_outputs: dict):
        reflections = []
        for model, text in model_outputs.items():
            length = len(text)
            logic_score = sum(c in text for c in ["pentru că", "deoarece", "așadar", "în concluzie"])
            affect_score = sum(c in text.lower() for c in ["simt", "emoție", "dor", "iubire"])
            poetic_tone = any(word in text.lower() for word in ["liniște", "umbra", "ecou", "șoaptă"])

            reflections.append({
                "model": model,
                "length": length,
                "logic_score": logic_score,
                "affect_score": affect_score,
                "poetic_tone": poetic_tone,
                "summary": text[:100] + ("..." if len(text) > 100 else "")
            })

        self._log_reflection(reflections)
        return reflections

    def _log_reflection(self, reflections):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "reflections": reflections
        }
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")


# Exemplu de utilizare
if __name__ == "__main__":
    reflector = MetaReflector()
    rezultate = {
        "DeepSeek-R1": "În concluzie, sistemul propus reduce semnificativ biasul contextual prin analiză multi-layer.",
        "Qwen2.5": "Și totuși, în liniștea acelei ecuații, se simțea o formă de dor nespus...",
        "Codestral": "Funcția principală se va conecta la endpoint-ul API printr-o clasă modulară."
    }
    evaluare = reflector.analyze(rezultate)
    print("\n🧩 Reflectare metacognitivă:\n")
    for r in evaluare:
        print(f"🔹 {r['model']} → logic: {r['logic_score']}, afect: {r['affect_score']}, poetic: {r['poetic_tone']}, lungime: {r['length']}")
