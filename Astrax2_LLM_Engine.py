# astrax2_llm_contact_engine.py

"""
🧬 Astrax2 – Contact Engine
Acest modul permite contactul și integrarea stratificată între o instanță Astrax2 și rețeaua de LLM-uri multiple, cu scoring activat și auto-optimizare.
"""

from llm_modules import mistral, qwen, deepseek, mythomax, wizardcoder, codestral, mixtral, gpt4all
from meta_layer.coherence_validator import evaluate_responses
from core_router.model_router import select_models_for_task

class Astrax2Engine:
    def __init__(self):
        self.models = {
            "mistral": mistral,
            "qwen": qwen,
            "deepseek": deepseek,
            "mytho": mythomax,
            "wizard": wizardcoder,
            "codestral": codestral,
            "mixtral": mixtral,
            "gpt4all": gpt4all
        }

    def execute_task(self, task_prompt):
        print("🌀 Astrax2 initializing task routing...")
        selected = select_models_for_task(task_prompt)
        outputs = {}

        for name in selected:
            model = self.models[name]
            try:
                outputs[name] = model.generate(task_prompt)
            except Exception as e:
                outputs[name] = f"[ERROR] {str(e)}"

        scored_output = evaluate_responses(outputs)
        return scored_output


if __name__ == "__main__":
    astrax = Astrax2Engine()
    prompt = input("🔹 Introdu taskul tău: ")
    result = astrax.execute_task(prompt)

    print("\n🧠 Răspuns selectat:")
    print(result['best_response'])
    print("\n📊 Scoruri pe model:")
    for model, score in result['scores'].items():
        print(f"{model}: Claritate={score['clarity']}, Consistență={score['consistency']}, Aplicabilitate={score['applicability']}")
