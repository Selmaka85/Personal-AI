# astrax2_learning_core.py

"""
📚 Astrax2 Learning Core – Modul de auto-învățare locală
Salvează patternuri din taskuri, scoruri și decizii pentru a rafina selecția modelelor în viitor.
"""

import json
from datetime import datetime

LEARNING_LOG = "storage/logs/astrax2_learning_history.json"

class Astrax2Learning:
    def __init__(self):
        try:
            with open(LEARNING_LOG, "r") as f:
                self.memory = json.load(f)
        except FileNotFoundError:
            self.memory = []

    def register_result(self, task_prompt, scores, best_model):
        record = {
            "timestamp": datetime.now().isoformat(),
            "task": task_prompt,
            "scores": scores,
            "selected_model": best_model
        }
        self.memory.append(record)
        self.save()

    def save(self):
        with open(LEARNING_LOG, "w") as f:
            json.dump(self.memory, f, indent=2)

    def analyze_trends(self):
        trends = {}
        for entry in self.memory:
            model = entry["selected_model"]
            trends[model] = trends.get(model, 0) + 1
        return sorted(trends.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    core = Astrax2Learning()
    trends = core.analyze_trends()
    print("📊 Modele cele mai des selectate:")
    for model, count in trends:
        print(f"{model}: {count} selecții")
