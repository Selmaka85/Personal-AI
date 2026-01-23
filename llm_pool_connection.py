# nexus_efe_with_astra.py – Exemplu complet de integrare cu Astra Locală sau alt sistem

# 1. DEFINIREA MOCK-LLM-URILOR (pot fi înlocuite cu Llama.cpp, GPT4All, DeepSeek etc)

class DummyLLM:
    def __init__(self, name):
        self.name = name

    def generate(self, prompt):
        return f"[{self.name}] Output generat pentru: '{prompt}'"


# 2. CONFIGURARE LLM_POOL – simulare Astra împărțită pe funcții

llm_pool = {
    "code": DummyLLM("AstraCode"),
    "strategy": DummyLLM("AstraStrategic"),
    "emotion": DummyLLM("AstraAffectiva"),
    "default": DummyLLM("AstraDefault"),
    "backup": DummyLLM("AstraFallback")
}


# 3. CONFIG – praguri de decizie (se pot încărca din config.yaml/json)

config = {
    "thresholds": {"accept": 0.75}
}


# 4. IMPORTĂM NUCLEUL NEXUS (definit în nexus_efe_core_engine.py)
from nexus_efe_core_engine import NexusEFE


# 5. INSTANȚIEM ENGINE-UL
nexus_engine = NexusEFE(config=config, llm_pool=llm_pool)


# 6. DEFINIM UN SMART PARSER PENTRU INPUTURI

class AstraSmartParser:
    def parse(self, input_data):
        if any(x in input_data.lower() for x in ["python", "function", "sort"]):
            return {"type": "code", "content": input_data}
        elif any(x in input_data.lower() for x in ["plan", "mvp", "launch", "market"]):
            return {"type": "strategy", "content": input_data}
        elif any(x in input_data.lower() for x in ["feel", "emotion", "sad", "happy"]):
            return {"type": "emotion", "content": input_data}
        else:
            return {"type": "default", "content": input_data}

# Adăugăm parserul custom
nexus_engine.input_parser = AstraSmartParser()


# 7. TESTARE CU DIVERSE INPUTURI

tests = [
    "Please write a Python function to sort a list of integers",
    "Create a startup launch plan for a fitness AI app",
    "I feel sad and I don’t know what to do...",
    "Tell me a joke",
]

print("\n--- SIMULARE RĂSPUNSURI ASTRA ---\n")
for prompt in tests:
    output = nexus_engine.process(prompt)
    print(f"Prompt: {prompt}\n→ Răspuns: {output}\n")