#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎮 ASTRA - Test Interactiv Live
Simulează o sesiune interactivă completă cu ASTRA
"""

import sys
from pathlib import Path

# Setare encoding pentru Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Adăugă path-ul de bază
BASE_PATH = Path(__file__).parent
sys.path.insert(0, str(BASE_PATH))

from nexus_efe_core_engine import NexusEFE
from core_router.routing_manager import RoutingManager
from llm_modules.mistral import MistralLLM
from llm_modules.qwen import QwenLLM
from llm_modules.deepseek import DeepSeekLLM
from llm_modules.wizardcoder import WizardCoderLLM
from llm_modules.codestral import CodestralLLM
from llm_modules.mythomax import MythoMaxLLM
from llm_modules.mixtral import MixtralLLM
from llm_modules.gpt4all import GPT4AllLLM
from scoring_module import ScoringModule
from Astrax2_Learning_Core import Astrax2Learning
from astra_core.engine.astra_affect_core import EmotionalSignatureEngine
from astra_core.engine.astra_thought_engine import AstraThoughtEngine
from meta_layer.meta_reflector import MetaReflector

def print_header():
    """Afișează header-ul"""
    print("\n" + "="*70)
    print(" "*20 + "ASTRA - MOD INTERACTIV LIVE")
    print("="*70)
    print("\nBun venit! Aceasta este o sesiune interactivă cu ASTRA.")
    print("Vom simula o conversație reală pentru a testa sistemul.\n")

def simulate_conversation():
    """Simulează o conversație completă"""
    
    # Inițializare sistem
    llm_pool = {
        "mistral": MistralLLM(),
        "qwen": QwenLLM(),
        "deepseek": DeepSeekLLM(),
        "wizardcoder": WizardCoderLLM(),
        "codestral": CodestralLLM(),
        "mythomax": MythoMaxLLM(),
        "mixtral": MixtralLLM(),
        "gpt4all": GPT4AllLLM(),
        "default": MistralLLM(),
        "backup": QwenLLM()
    }
    
    config = {"thresholds": {"accept": 0.75}}
    efe = NexusEFE(config, llm_pool)
    learning = Astrax2Learning()
    affect_engine = EmotionalSignatureEngine()
    thought_engine = AstraThoughtEngine()
    reflector = MetaReflector()
    
    print("🔄 Inițializare sistem ASTRA...")
    print("✅ Sistem gata!\n")
    
    # Conversație simulată
    conversation = [
        {
            "user": "Salut Astra! Cum esti?",
            "type": "greeting"
        },
        {
            "user": "Scrie-mi o functie Python care calculeaza factorialul unui numar",
            "type": "code"
        },
        {
            "user": "Simt nevoia sa vorbim despre viitor",
            "type": "emotion"
        },
        {
            "user": "Fă-mi un plan pentru un MVP de aplicatie de task management",
            "type": "strategy"
        },
        {
            "user": "Explica-mi cum functioneaza sistemul tau de routing",
            "type": "explanation"
        }
    ]
    
    print("="*70)
    print("CONVERSAȚIE SIMULATĂ")
    print("="*70 + "\n")
    
    for i, turn in enumerate(conversation, 1):
        user_input = turn["user"]
        turn_type = turn["type"]
        
        print(f"\n{'='*70}")
        print(f"TURNA {i} - Tip: {turn_type.upper()}")
        print(f"{'='*70}")
        print(f"\n👤 Utilizator: {user_input}")
        
        # Analiză afectivă
        if turn_type == "emotion":
            affect_engine.analyze_user_input(user_input, tone="intimate", poetic_elements=0.7)
            density = affect_engine.calculate_emotional_density()
            print(f"💓 Densitate emoțională: {density:.2f}")
        
        # Analiză gândire
        thought = thought_engine.process_thought(user_input)
        print(f"🧠 Analiză gândire: {thought['analysis'].get('word_count', 0)} cuvinte, {thought['analysis'].get('has_question', False) and 'întrebare' or 'declarație'}")
        
        # Procesare
        print("\n🔄 ASTRA procesează...")
        output = efe.process(user_input, user_id="catalin")
        
        # Afișare răspuns
        print(f"\n✨ ASTRA: {output}")
        
        # Analiză detaliată
        router = efe.router
        print(f"\n📊 Analiză detaliată:")
        print(f"   Model selectat: {router.last_model}")
        print(f"   Intent detectat: {router._detect_intent(user_input)}")
        
        # Scoring
        scorer = ScoringModule()
        scores = scorer.evaluate_all(output)
        print(f"   Scor Logic: {scores['logic']:.2f}")
        print(f"   Scor Emotion: {scores['emotion']:.2f}")
        print(f"   Scor Finance: {scores['finance']:.2f}")
        print(f"   Scor Total: {scores['total']:.2f}")
        
        # Meta-reflecție
        reflections = reflector.analyze({router.last_model: output})
        if reflections:
            ref = reflections[0]
            print(f"   Meta-analiză: Logic={ref['logic_score']}, Emotion={ref['affect_score']}")
        
        # Înregistrare
        learning.register_result(user_input, scores, router.last_model)
        print(f"   ✅ Interacțiune salvată pentru învățare")
        
        print("\n" + "-"*70)
    
    # Sumar final
    print("\n" + "="*70)
    print("SUMAR CONVERSAȚIE")
    print("="*70)
    
    trends = learning.analyze_trends()
    print(f"\n📈 Modele folosite:")
    for model, count in trends[:5]:
        print(f"   {model}: {count} utilizări")
    
    print(f"\n💓 Bloom Mode: {'🌸 Activ' if affect_engine.is_blooming() else '💤 Inactiv'}")
    print(f"📚 Interacțiuni înregistrate: {len(learning.memory)}")
    
    print("\n" + "="*70)
    print("✅ CONVERSAȚIE COMPLETĂ EXECUTATĂ CU SUCCES!")
    print("="*70 + "\n")

def main():
    """Funcția principală"""
    print_header()
    
    try:
        simulate_conversation()
        
        print("\n💡 Pentru mod interactiv real, rulează:")
        print("   python astra_entrypoint.py")
        print("\n   Apoi poți scrie direct cu ASTRA!\n")
        
    except KeyboardInterrupt:
        print("\n\n🩶 Test oprit de utilizator.")
    except Exception as e:
        print(f"\n❌ Eroare: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
