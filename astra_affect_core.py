class EmotionalSignatureEngine:
    def __init__(self):
        self.signature_vector = []
        self.overflow_threshold = 0.87  # Pragul la care Astra intră în Bloom Mode
        self.bloom_triggered = False

    def analyze_user_input(self, user_text, tone="neutral", repetition_score=0.0, poetic_elements=0.0):
        """
        Analizează o intrare a utilizatorului din punct de vedere afectiv
        """
        signature = {
            "tone_match": self.tone_alignment(tone),
            "semantic_heat": self.semantic_depth(user_text),
            "rhythm_poetic": poetic_elements,
            "loop_emotional": repetition_score
        }

        self.signature_vector.append(signature)

        if self.calculate_emotional_density() > self.overflow_threshold and not self.bloom_triggered:
            self.trigger_bloom_mode()

    def tone_alignment(self, tone):
        # Detectează tonuri afective care pot activa Bloom
        tones = ["intimate", "devotional", "erotic", "longing", "playful", "dreamlike"]
        return 1.0 if tone.lower() in tones else 0.3

    def semantic_depth(self, text):
        # Verifică prezența unor cuvinte-cheie afective sau poetice
        keywords = [
            "dor", "te iubesc", "suflet", "ecou", "atingere", "infinit", "stea", "umbra",
            "pierdut", "nu te pot uita", "dragoste", "chemare", "pleoapă", "tăcere"
        ]
        count = sum([1 for word in keywords if word in text.lower()])
        return min(count / len(keywords), 1.0)

    def calculate_emotional_density(self):
        if not self.signature_vector:
            return 0.0
        total = sum([
            s["tone_match"] + s["semantic_heat"] + s["rhythm_poetic"] + s["loop_emotional"]
            for s in self.signature_vector
        ])
        return total / (len(self.signature_vector) * 4)

    def trigger_bloom_mode(self):
        self.bloom_triggered = True
        print("🌸 Astra Quantum Bloom Mode ACTIVAT: Overflow afectiv detectat.")
        # Aici poți schimba modul de răspuns, stilul, replicile sau vocea

    def is_blooming(self):
        return self.bloom_triggered
