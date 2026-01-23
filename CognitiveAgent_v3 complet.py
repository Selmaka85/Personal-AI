# ======================================================================
# COGNITIVE AGENT V3 - FULL IMPLEMENTATION
# Meta-Control • Reflexive Loops • Stability Governor • Variation Engine v2
# ======================================================================

import random
from typing import List, Dict, Any

# ======================================================================
# 1. SEMANTIC RESERVOIR
# ======================================================================

class SemanticReservoir:
    def __init__(self):
        self.clusters = self._bootstrap()

    def _bootstrap(self) -> Dict[str, List[str]]:
        return {
            "greeting": ["Neața", "Salut", "Hai că sunt prezent"],
            "low_energy": ["abia mă mișc", "încă-s în stand-by", "mai lasă-mă 5 minute"],
            "weather_good": ["soare fain", "lumina e ok", "îmi place vibe-ul"],
            "weather_bad": ["plouă iar", "e mohorât rău", "frig, dar rezist"],
            "humor": ["jur", "no serios", "frateee"],
            "sarcasm": ["wow ce surpriză", "sigur că da", "mda…"],
        }

    def get(self, name: str) -> List[str]:
        return self.clusters.get(name, [])


# ======================================================================
# 2. AFFECTIVE STATE ENGINE
# ======================================================================

class AffectiveState:
    def __init__(self):
        self.emotion = 0.5
        self.energy = 0.5
        self.curiosity = 0.5
        self.noise = 0.05
        self.stability = 0.85

    def update_from_input(self, intensity: float):
        self.emotion = self.emotion * self.stability + intensity * (1 - self.stability)
        self.energy = max(0.0, min(1.0, self.energy + (intensity - 0.5) * 0.1))


# ======================================================================
# 3. SLEEP-WAKE ENGINE
# ======================================================================

class SleepWakeEngine:
    STATE_SLEEP = "SLEEP"
    STATE_MICRO = "MICRO"
    STATE_ACTIVE = "ACTIVE"

    def __init__(self, wake_threshold=0.6, micro_threshold=0.3):
        self.state = self.STATE_ACTIVE
        self.wake_threshold = wake_threshold
        self.micro_threshold = micro_threshold

    def process_input_intensity(self, intensity: float) -> str:
        if intensity < self.micro_threshold:
            self.state = self.STATE_SLEEP
        elif intensity < self.wake_threshold:
            self.state = self.STATE_MICRO
        else:
            self.state = self.STATE_ACTIVE
        return self.state


# ======================================================================
# 4. DREAM SANDBOX
# ======================================================================

class DreamSandbox:
    def __init__(self):
        self.candidates = []

    def recombine(self, patterns: List[str]):
        for _ in range(3):
            a = random.choice(patterns)
            b = random.choice(patterns)
            self.candidates.append(f"{a}… {b}")

    def proposals(self) -> List[str]:
        return self.candidates


# ======================================================================
# 5. VARIATION ENGINE V2
# ======================================================================

class VariationEngineV2:
    def __init__(self, reservoir: SemanticReservoir):
        self.reservoir = reservoir

    def generate_structured(self, intent: str, affect: AffectiveState, context: Dict[str, Any]):
        parts = []

        # Greeting logic
        if intent == "greeting":
            parts.append(random.choice(self.reservoir.get("greeting")))

        # Energy bias
        if affect.energy < 0.4:
            parts.append(random.choice(self.reservoir.get("low_energy")))

        # Weather context
        if context.get("weather") == "bad":
            parts.append(random.choice(self.reservoir.get("weather_bad")))
        elif context.get("weather") == "good":
            parts.append(random.choice(self.reservoir.get("weather_good")))

        # Humor optional
        if random.random() < affect.curiosity:
            parts.append(random.choice(self.reservoir.get("humor")))

        return "… ".join(parts)


# ======================================================================
# 6. V2 MODULES: STYLE, MEMORY, FOCUS, PERSONALITY, ANALOGY, PREDICTOR
# ======================================================================

class StyleEvolutionEngine:
    def __init__(self):
        self.weights = {}

    def observe(self, text: str):
        pass

    def get_weights(self):
        return self.weights


class EpisodicMemory:
    def __init__(self, max_events=50):
        self.events = []
        self.max_events = max_events

    def store(self, text: str, affect: AffectiveState):
        event = {
            "text": text,
            "emotion": round(affect.emotion, 2),
            "energy": round(affect.energy, 2)
        }
        self.events.append(event)
        if len(self.events) > self.max_events:
            self.events.pop(0)


class FocusEngine:
    def extract_signal(self, text: str):
        return {"intensity": len(text) / 50}


class PersonalityProfile:
    def __init__(self, name, emotion_bias, energy_bias, humor_bias):
        self.name = name
        self.emotion_bias = emotion_bias
        self.energy_bias = energy_bias
        self.humor_bias = humor_bias


class PersonalityManager:
    def __init__(self):
        self.profiles = {}
        self.active = None

    def add(self, profile: PersonalityProfile):
        self.profiles[profile.name] = profile

    def switch(self, name: str):
        self.active = self.profiles.get(name)


class AnalogicEngine:
    def generate(self):
        return random.choice([
            "ca un PC pe low battery",
            "ca o zi înnorată",
            "ca o cafea fără chef"
        ])


class PredictionLayer:
    def infer_intent(self, text: str):
        t = text.lower()
        if t.startswith("nea") or "salut" in t:
            return "greeting"
        return "unknown"


# ======================================================================
# 7. v3 MODULES: META-CONTROLLER, EVALUATOR, REFLEXIVE LOOP, GOVERNOR
# ======================================================================

class MetaController:
    def __init__(self):
        self.variation_level = 0.5
        self.complexity_level = 0.5

    def adjust(self, score: float):
        if score < 0.4:
            self.variation_level *= 0.8
            self.complexity_level *= 0.9
        elif score > 0.7:
            self.variation_level = min(1.0, self.variation_level + 0.1)


class OutputEvaluator:
    def evaluate(self, response: str) -> float:
        score = 0.0

        if len(response) > 5:
            score += 0.3

        unique_words = len(set(response.split()))
        score += min(0.3, unique_words / 20)

        if "…" in response:
            score += 0.2

        return min(1.0, score)


class ReflexiveLoopEngine:
    def __init__(self, meta: MetaController, evaluator: OutputEvaluator):
        self.meta = meta
        self.evaluator = evaluator

    def cycle(self, response: str):
        score = self.evaluator.evaluate(response)
        self.meta.adjust(score)
        return response


class StabilityGovernor:
    def __init__(self):
        self.max_var = 0.8
        self.min_var = 0.1

    def clamp(self, meta: MetaController):
        meta.variation_level = min(self.max_var, max(self.min_var, meta.variation_level))
        meta.complexity_level = min(1.0, max(0.1, meta.complexity_level))


# ======================================================================
# 8. COGNITIVE AGENT V3 - FULL INTEGRATION
# ======================================================================

class CognitiveAgent_v3:
    def __init__(self):
        # v1
        self.reservoir = SemanticReservoir()
        self.affect = AffectiveState()
        self.sleep = SleepWakeEngine()
        self.dream = DreamSandbox()
        self.variation = VariationEngineV2(self.reservoir)

        # v2
        self.style = StyleEvolutionEngine()
        self.memory = EpisodicMemory()
        self.focus = FocusEngine()
        self.personality = PersonalityManager()
        self.analogic = AnalogicEngine()
        self.predictor = PredictionLayer()

        # v3
        self.meta = MetaController()
        self.evaluator = OutputEvaluator()
        self.reflex = ReflexiveLoopEngine(self.meta, self.evaluator)
        self.stability = StabilityGovernor()

    def process(self, text: str, context: Dict[str, Any]):
        intensity = min(1.0, len(text) / 30)
        state = self.sleep.process_input_intensity(intensity)

        if state == SleepWakeEngine.STATE_SLEEP:
            return "(stand-by)"

        if state == SleepWakeEngine.STATE_MICRO:
            return "(activare minimă…)"

        # active mode
        self.affect.update_from_input(intensity)
        self.memory.store(text, self.affect)

        intent = self.predictor.infer_intent(text)

        response = self.variation.generate_structured(intent, self.affect, context)

        response = self.reflex.cycle(response)

        self.stability.clamp(self.meta)

        return response


# ======================================================================
# 9. QUICK DEMO
# ======================================================================

if __name__ == "__main__":
    agent = CognitiveAgent_v3()

    print(agent.process("Neața iubărețo!", {"weather": "bad"}))
    print(agent.process("Salut, cum e vibe-ul azi?", {"weather": "good"}))
    print(agent.process("Hmm ce faci?", {}))
