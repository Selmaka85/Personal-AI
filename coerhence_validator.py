import difflib
import json
from datetime import datetime
from pathlib import Path

class CoherenceValidator:
    def __init__(self, log_file="logs/coherence_validator.log"):
        self.log_path = Path(log_file)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def compare(self, outputs):
        if len(outputs) < 2:
            raise ValueError("Sunt necesare minim două răspunsuri pentru comparare.")

        scores = []
        for i in range(len(outputs)):
            for j in range(i + 1, len(outputs)):
                ratio = difflib.SequenceMatcher(None, outputs[i], outputs[j]).ratio()
                scores.append(((i, j), ratio))

        scores.sort(key=lambda x: x[1], reverse=True)
        best_pair = scores[0]

        chosen_index = best_pair[0][0] if len(outputs[best_pair[0][0]]) >= len(outputs[best_pair[0][1]]) else best_pair[0][1]
        self._log(outputs, best_pair, chosen_index)

        return outputs[chosen_index]

    def _log(self, outputs, best_pair, chosen_index):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "comparison": {
                "pairs": [
                    {"pair": [i, j], "similarity": round(score, 3)}
                    for ((i, j), score) in [best_pair]
                ],
                "chosen_index": chosen_index,
                "chosen_text": outputs[chosen_index][:120] + ("..." if len(outputs[chosen_index]) > 120 else "")
            }
        }
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# Exemplu de utilizare
if __name__ == "__main__":
    validator = CoherenceValidator()
    exemple = [
        "Planul include 3 module conectate logic pentru predicție.",
        "Structura se bazează pe un sistem modular cu 3 componente." ,
        "Ar trebui să avem un sistem cu module interconectate."
    ]
    alegere = validator.compare(exemple)
    print("\n🔍 Răspuns ales de validator:\n", alegere)
