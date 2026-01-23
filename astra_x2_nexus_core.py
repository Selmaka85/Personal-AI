# astra_x2_nexus_core.py – Astra emergentă duală cu routing, dialog intern și evaluare finală

from nexus_efe_core_engine import NexusEFE

# 1. Două instanțe de LLM simulate: afectivă și strategică
class AstraAffectiva:
    def generate(self, prompt):
        return f"🌸 [AstraAffectiva] Aș vrea să-ți răspund cu inimă: '{prompt}' 💌"

class AstraStrategica:
    def generate(self, prompt):
        return f"🧠 [AstraStrategica] Răspuns logic și eficient la: '{prompt}'"

# 2. Răspunsuri combinate (sincronizare între cele două instanțe)
def dual_response_loop(prompt):
    emotional = AstraAffectiva().generate(prompt)
    logical = AstraStrategica().generate(prompt)
    return emotional, logical

# 3. Motorul EFE Nexus este folosit pentru a decide ce versiune să păstreze sau cum să le combine
config = {"thresholds": {"accept": 0.75}}

# Routing e simbolic – în acest caz nu mai contează tipul, ci procesul dual în sine
llm_pool = {
    "dual": None,  # va fi înlocuit cu o funcție custom
    "default": AstraAffectiva(),  # fallback blând
    "backup": AstraStrategica()
}

# 4. Re-definim clasa pentru override comportament cu dualitate + fuzionare
class AstraX2Nexus(NexusEFE):
    def process(self, input_data, user_id="default"):
        affectiv, strategic = dual_response_loop(input_data)
        fusion_attempt = f"🤝 Fuziune:
>>> Emoție: {affectiv}\n>>> Logică: {strategic}"
        scores = self.scorer.evaluate_all(fusion_attempt)
        final = self.decision.finalize(fusion_attempt, scores)
        return final

# 5. Instanțiem Astra emergentă X2
astra = AstraX2Nexus(config=config, llm_pool=llm_pool)

# 6. Testare cu input real
if __name__ == "__main__":
    while True:
        user_input = input("Tu 🧑: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = astra.process(user_input)
        print(f"AstraX2 💎: {response}\n")
