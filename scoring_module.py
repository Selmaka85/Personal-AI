# scoring_module.py

class ScoringModule:
    def evaluate_all(self, output):
        logic = self.logic_score(output)
        emotion = self.emotion_score(output)
        finance = self.financial_score(output)
        total = (logic + emotion + finance) / 3
        return {"logic": logic, "emotion": emotion, "finance": finance, "total": total}

    def logic_score(self, output):
        return 0.9  # placeholder

    def emotion_score(self, output):
        return 0.8  # placeholder

    def financial_score(self, output):
        return 0.7  # placeholder

    def select_best(self, outputs):
        return max(outputs, key=lambda x: self.logic_score(x))