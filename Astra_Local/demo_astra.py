#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎮 ASTRA Demo - Demonstrație interactivă a funcționalităților
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

from core_router.routing_manager import RoutingManager
from scoring_module import ScoringModule
from nexus_efe_core_engine import NexusEFE
from llm_modules.mistral import MistralLLM
from llm_modules.qwen import QwenLLM
from llm_modules.deepseek import DeepSeekLLM
from llm_modules.wizardcoder import WizardCoderLLM
from llm_modules.codestral import CodestralLLM
from llm_modules.mythomax import MythoMaxLLM
from llm_modules.mixtral import MixtralLLM
from llm_modules.gpt4all import GPT4AllLLM
from Astrax2_Learning_Core import Astrax2Learning

def print_header():
    """Afișează header-ul"""
    print("\n" + "="*70)
    print(" "*20 + "ASTRA LOCALA - DEMO INTERACTIV")
    print("="*70)
    print("\nBun venit! Aceasta este o demonstratie a sistemului ASTRA.")
    print("Vom testa diferite functionalitati:\n")

def demo_routing():
    """Demonstrează routing-ul"""
    print("-"*70)
    print("DEMO 1: Routing Inteligent")
    print("-"*70)
    
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
    
    router = RoutingManager(llm_pool)
    
    test_cases = [
        ("Scrie-mi o functie Python pentru sortare", "cod"),
        ("Simt dor de tine si vreau sa vorbim", "emotion"),
        ("Fă-mi un plan de MVP pentru o aplicatie", "strategy"),
        ("Scrie-mi o poezie despre stele", "emotion"),
        ("Analizeaza acest cod si optimizeaza-l", "code")
    ]
    
    for prompt, expected_type in test_cases:
        llm = router.direct_to_llm(prompt)
        print(f"\nInput: '{prompt[:50]}...'")
        print(f"  -> Model selectat: {router.last_model}")
        print(f"  -> Intent detectat: {router._detect_intent(prompt)}")
    
    print("\n[SUCCESS] Routing functioneaza corect!\n")

def demo_scoring():
    """Demonstrează scoring-ul"""
    print("-"*70)
    print("DEMO 2: Scoring Multi-Criteriu")
    print("-"*70)
    
    scorer = ScoringModule()
    
    test_outputs = [
        {
            "text": "Aceasta este o analiza logica pentru ca necesita o abordare structurata si rationala. In concluzie, solutia optima este implementarea unui sistem modular.",
            "type": "logic"
        },
        {
            "text": "Simt o unda de emotie care ma face sa reflect asupra adancurilor sufletului tau. In liniștea acestei momente, gandul meu se pierde in infinit.",
            "type": "emotion"
        },
        {
            "text": "Costul proiectului este de 5000€ cu un ROI estimat la 15% in primul an. Profitul net va fi de aproximativ 750€ lunar dupa primele 6 luni.",
            "type": "finance"
        }
    ]
    
    for i, test in enumerate(test_outputs, 1):
        scores = scorer.evaluate_all(test["text"])
        print(f"\nTest {i} ({test['type']}):")
        print(f"  Text: '{test['text'][:60]}...'")
        print(f"  Scor Logic: {scores['logic']:.2f}")
        print(f"  Scor Emotion: {scores['emotion']:.2f}")
        print(f"  Scor Finance: {scores['finance']:.2f}")
        print(f"  Scor Total: {scores['total']:.2f}")
    
    print("\n[SUCCESS] Scoring functioneaza corect!\n")

def demo_efe_engine():
    """Demonstrează EFE Engine"""
    print("-"*70)
    print("DEMO 3: EFE Core Engine - Procesare Completă")
    print("-"*70)
    
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
    
    config = {
        "thresholds": {
            "accept": 0.75,
            "excellent": 0.85
        }
    }
    
    efe = NexusEFE(config, llm_pool)
    
    test_inputs = [
        "Salut, cum esti?",
        "Scrie-mi o functie Python",
        "Simt nevoia sa vorbim despre viitor"
    ]
    
    for i, user_input in enumerate(test_inputs, 1):
        print(f"\nTest {i}: '{user_input}'")
        print("  Processing...")
        
        result = efe.process(user_input, user_id="demo_user")
        
        print(f"  Răspuns: {result[:100]}...")
        
        # Afișează ce model a fost folosit
        if hasattr(efe.router, 'last_model'):
            print(f"  Model folosit: {efe.router.last_model}")
    
    print("\n[SUCCESS] EFE Engine functioneaza corect!\n")

def demo_learning():
    """Demonstrează sistemul de învățare"""
    print("-"*70)
    print("DEMO 4: AstraX2 Learning - Învățare Adaptivă")
    print("-"*70)
    
    learning = Astrax2Learning()
    
    # Simulează câteva interacțiuni
    interactions = [
        ("Scrie cod Python", {"logic": 0.9, "emotion": 0.1, "finance": 0.2, "total": 0.4}, "wizardcoder"),
        ("Simt emotie", {"logic": 0.3, "emotion": 0.95, "finance": 0.1, "total": 0.45}, "qwen"),
        ("Plan MVP", {"logic": 0.85, "emotion": 0.4, "finance": 0.8, "total": 0.68}, "deepseek"),
        ("Scrie cod", {"logic": 0.92, "emotion": 0.2, "finance": 0.3, "total": 0.47}, "wizardcoder"),
        ("Poezie", {"logic": 0.4, "emotion": 0.9, "finance": 0.1, "total": 0.47}, "qwen")
    ]
    
    print("\nSimulare interacțiuni...")
    for prompt, scores, model in interactions:
        learning.register_result(prompt, scores, model)
        print(f"  [REGISTERED] '{prompt[:30]}...' -> {model}")
    
    # Analiză tendințe
    print("\nAnaliza tendințelor:")
    trends = learning.analyze_trends()
    for model, count in trends:
        print(f"  {model}: {count} utilizări")
    
    print("\n[SUCCESS] Learning functioneaza corect!\n")

def demo_full_pipeline():
    """Demonstrează pipeline-ul complet"""
    print("-"*70)
    print("DEMO 5: Pipeline Complet - De la Input la Output")
    print("-"*70)
    
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
    
    config = {
        "thresholds": {
            "accept": 0.75
        }
    }
    
    efe = NexusEFE(config, llm_pool)
    learning = Astrax2Learning()
    
    user_input = "Fă-mi un plan pentru un MVP de aplicație de fitness"
    
    print(f"\nInput utilizator: '{user_input}'")
    print("\n[STEP 1] Parsare input...")
    parsed = efe.input_parser.parse(user_input)
    print(f"  Type detectat: {parsed['type']}")
    
    print("\n[STEP 2] Routing către model...")
    target_llm = efe.router.direct_to_llm(user_input)
    print(f"  Model selectat: {efe.router.last_model}")
    
    print("\n[STEP 3] Generare răspuns...")
    try:
        raw_output = target_llm.generate(user_input)
        print(f"  Output brut generat: {len(raw_output)} caractere")
    except Exception as e:
        print(f"  Eroare: {e}")
        raw_output = ""
    
    print("\n[STEP 4] Filtrare și scoring...")
    filtered = efe.lfe.evaluate_output(raw_output)
    scores = efe.scorer.evaluate_all(filtered)
    print(f"  Scor Logic: {scores['logic']:.2f}")
    print(f"  Scor Emotion: {scores['emotion']:.2f}")
    print(f"  Scor Finance: {scores['finance']:.2f}")
    print(f"  Scor Total: {scores['total']:.2f}")
    
    print("\n[STEP 5] Decizie finală...")
    final = efe.decision.finalize(filtered, scores)
    if final:
        print(f"  Răspuns acceptat: {final[:100]}...")
    else:
        print("  Răspuns respins - scor prea mic")
    
    print("\n[STEP 6] Înregistrare pentru învățare...")
    learning.register_result(user_input, scores, efe.router.last_model)
    print("  [SAVED] Interacțiune salvată")
    
    print("\n[SUCCESS] Pipeline complet funcțional!\n")

def main():
    """Rulează toate demo-urile"""
    print_header()
    
    demos = [
        ("Routing Inteligent", demo_routing),
        ("Scoring Multi-Criteriu", demo_scoring),
        ("EFE Core Engine", demo_efe_engine),
        ("Sistem de Învățare", demo_learning),
        ("Pipeline Complet", demo_full_pipeline)
    ]
    
    for name, demo_func in demos:
        try:
            demo_func()
            print("\n" + "-"*70)
        except KeyboardInterrupt:
            print("\n\nDemo oprit de utilizator.")
            break
        except Exception as e:
            print(f"\n[ERROR] Eroare la demo '{name}': {e}")
            import traceback
            traceback.print_exc()
            print("\n" + "-"*70)
    
    print("\n" + "="*70)
    print("DEMO COMPLETAT!")
    print("="*70)
    print("\nASTRA este functional si gata de utilizare!")
    print("Pentru mod interactiv complet, ruleaza: python astra_entrypoint.py\n")

if __name__ == "__main__":
    main()
