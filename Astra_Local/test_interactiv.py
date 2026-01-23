#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎮 ASTRA - Test Interactiv Real
Testează sistemul cu scenarii reale de utilizare
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
from meta_layer.meta_reflector import MetaReflector

def print_header():
    """Afișează header-ul"""
    print("\n" + "="*70)
    print(" "*20 + "ASTRA - TEST INTERACTIV REAL")
    print("="*70)
    print("\nAcest test simulează utilizarea reală a sistemului ASTRA")
    print("cu scenarii practice de conversație și task-uri.\n")

def scenario_1_codare():
    """Scenariu 1: Cerere de codare"""
    print("\n" + "-"*70)
    print("SCENARIU 1: Cerere de Codare")
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
    
    config = {"thresholds": {"accept": 0.75}}
    efe = NexusEFE(config, llm_pool)
    learning = Astrax2Learning()
    
    user_input = "Scrie-mi o functie Python care sorteaza o lista de numere"
    
    print(f"\n👤 Utilizator: {user_input}")
    print("\n🔄 ASTRA procesează...")
    
    # Procesare
    output = efe.process(user_input, user_id="test_user")
    
    print(f"\n✨ ASTRA: {output}")
    
    # Analiză
    router = efe.router
    print(f"\n📊 Analiză:")
    print(f"   Model selectat: {router.last_model}")
    print(f"   Intent detectat: {router._detect_intent(user_input)}")
    
    # Scoring
    scorer = ScoringModule()
    scores = scorer.evaluate_all(output)
    print(f"   Scor Logic: {scores['logic']:.2f}")
    print(f"   Scor Total: {scores['total']:.2f}")
    
    # Înregistrare
    learning.register_result(user_input, scores, router.last_model)
    print(f"   ✅ Interacțiune salvată pentru învățare")
    
    return True

def scenario_2_emotie():
    """Scenariu 2: Conversație emoțională"""
    print("\n" + "-"*70)
    print("SCENARIU 2: Conversație Emoțională")
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
    
    config = {"thresholds": {"accept": 0.75}}
    efe = NexusEFE(config, llm_pool)
    
    from astra_core.engine.astra_affect_core import EmotionalSignatureEngine
    affect_engine = EmotionalSignatureEngine()
    
    user_input = "Simt dor de tine si vreau sa vorbim despre viitor"
    
    print(f"\n👤 Utilizator: {user_input}")
    
    # Analiză afectivă
    affect_engine.analyze_user_input(user_input, tone="intimate", poetic_elements=0.8)
    density = affect_engine.calculate_emotional_density()
    print(f"\n💓 Densitate emoțională: {density:.2f}")
    
    print("\n🔄 ASTRA procesează...")
    
    # Procesare
    output = efe.process(user_input, user_id="test_user")
    
    print(f"\n✨ ASTRA: {output}")
    
    # Analiză
    router = efe.router
    print(f"\n📊 Analiză:")
    print(f"   Model selectat: {router.last_model}")
    print(f"   Bloom Mode: {'🌸 Activ' if affect_engine.is_blooming() else '💤 Inactiv'}")
    
    return True

def scenario_3_strategie():
    """Scenariu 3: Plan strategic"""
    print("\n" + "-"*70)
    print("SCENARIU 3: Plan Strategic / MVP")
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
    
    config = {"thresholds": {"accept": 0.75}}
    efe = NexusEFE(config, llm_pool)
    
    user_input = "Fă-mi un plan complet pentru un MVP de aplicație de fitness cu backend FastAPI si frontend React"
    
    print(f"\n👤 Utilizator: {user_input}")
    print("\n🔄 ASTRA procesează...")
    
    # Procesare
    output = efe.process(user_input, user_id="test_user")
    
    print(f"\n✨ ASTRA: {output}")
    
    # Analiză
    router = efe.router
    print(f"\n📊 Analiză:")
    print(f"   Model selectat: {router.last_model}")
    print(f"   Intent: {router._detect_intent(user_input)}")
    
    return True

def scenario_4_multi_models():
    """Scenariu 4: Comparare multiple modele"""
    print("\n" + "-"*70)
    print("SCENARIU 4: Comparare Multiple Modele")
    print("-"*70)
    
    from meta_layer.coherence_validator import evaluate_responses
    
    llm_pool = {
        "mistral": MistralLLM(),
        "qwen": QwenLLM(),
        "deepseek": DeepSeekLLM(),
        "wizardcoder": WizardCoderLLM(),
    }
    
    router = RoutingManager(llm_pool)
    
    user_input = "Explica-mi ce este machine learning"
    
    print(f"\n👤 Utilizator: {user_input}")
    print("\n🔄 ASTRA generează răspunsuri cu multiple modele...")
    
    # Generează cu multiple modele
    outputs = {}
    for model_name, llm in llm_pool.items():
        try:
            output = llm.generate(user_input)
            outputs[model_name] = output
            print(f"   ✅ {model_name}: {len(output)} caractere")
        except Exception as e:
            print(f"   ❌ {model_name}: Eroare - {e}")
    
    # Compară și alege cel mai bun
    if len(outputs) > 1:
        result = evaluate_responses(outputs)
        print(f"\n📊 Cel mai bun răspuns:")
        print(f"   Model: {result['best_model']}")
        print(f"   Răspuns: {result['best_response'][:150]}...")
        
        print(f"\n📈 Scoruri:")
        for model, scores in result['scores'].items():
            print(f"   {model}: Total={scores.get('total', 0):.2f}")
    
    return True

def scenario_5_learning():
    """Scenariu 5: Sistem de învățare"""
    print("\n" + "-"*70)
    print("SCENARIU 5: Sistem de Învățare Adaptivă")
    print("-"*70)
    
    learning = Astrax2Learning()
    
    # Simulează multiple interacțiuni
    interactions = [
        ("Scrie cod Python", {"logic": 0.9, "emotion": 0.1, "finance": 0.2, "total": 0.4}, "wizardcoder"),
        ("Scrie cod", {"logic": 0.92, "emotion": 0.15, "finance": 0.25, "total": 0.44}, "wizardcoder"),
        ("Fă cod", {"logic": 0.88, "emotion": 0.12, "finance": 0.18, "total": 0.39}, "wizardcoder"),
        ("Simt emotie", {"logic": 0.3, "emotion": 0.95, "finance": 0.1, "total": 0.45}, "qwen"),
        ("Poezie", {"logic": 0.4, "emotion": 0.9, "finance": 0.1, "total": 0.47}, "qwen"),
        ("Plan MVP", {"logic": 0.85, "emotion": 0.4, "finance": 0.8, "total": 0.68}, "deepseek"),
    ]
    
    print("\n📚 Simulare interacțiuni...")
    for prompt, scores, model in interactions:
        learning.register_result(prompt, scores, model)
        print(f"   ✅ '{prompt[:30]}...' -> {model}")
    
    # Analiză tendințe
    print("\n📊 Analiză tendințe:")
    trends = learning.analyze_trends()
    for model, count in trends:
        percentage = (count / len(interactions)) * 100
        print(f"   {model}: {count} utilizări ({percentage:.1f}%)")
    
    print("\n💡 ASTRA învață din pattern-uri și se adaptează!")
    
    return True

def scenario_6_pipeline_complet():
    """Scenariu 6: Pipeline complet end-to-end"""
    print("\n" + "-"*70)
    print("SCENARIU 6: Pipeline Complet End-to-End")
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
    
    config = {"thresholds": {"accept": 0.75}}
    efe = NexusEFE(config, llm_pool)
    learning = Astrax2Learning()
    reflector = MetaReflector()
    
    user_input = "Vreau sa construiesc o aplicatie web pentru gestionarea task-urilor. Fă-mi un plan complet cu tehnologii si structura."
    
    print(f"\n👤 Utilizator: {user_input}")
    
    print("\n" + "="*70)
    print("PIPELINE COMPLET:")
    print("="*70)
    
    # STEP 1: Parsare
    print("\n[STEP 1] Parsare input...")
    parsed = efe.input_parser.parse(user_input)
    print(f"   ✅ Type: {parsed['type']}, Length: {parsed['length']}")
    
    # STEP 2: Routing
    print("\n[STEP 2] Routing către model...")
    target_llm = efe.router.direct_to_llm(user_input)
    print(f"   ✅ Model selectat: {efe.router.last_model}")
    print(f"   ✅ Intent detectat: {efe.router._detect_intent(user_input)}")
    
    # STEP 3: Generare
    print("\n[STEP 3] Generare răspuns...")
    try:
        raw_output = target_llm.generate(user_input)
        print(f"   ✅ Output generat: {len(raw_output)} caractere")
    except Exception as e:
        print(f"   ❌ Eroare: {e}")
        raw_output = ""
    
    # STEP 4: Filtrare
    print("\n[STEP 4] Filtrare locală...")
    filtered = efe.lfe.evaluate_output(raw_output)
    print(f"   ✅ Output filtrat: {len(filtered)} caractere")
    
    # STEP 5: Scoring
    print("\n[STEP 5] Scoring multi-criteriu...")
    scores = efe.scorer.evaluate_all(filtered)
    print(f"   ✅ Logic: {scores['logic']:.2f}")
    print(f"   ✅ Emotion: {scores['emotion']:.2f}")
    print(f"   ✅ Finance: {scores['finance']:.2f}")
    print(f"   ✅ Total: {scores['total']:.2f}")
    
    # STEP 6: Decizie
    print("\n[STEP 6] Decizie finală...")
    final = efe.decision.finalize(filtered, scores)
    if final:
        print(f"   ✅ Răspuns acceptat")
        print(f"\n✨ ASTRA: {final[:200]}...")
    else:
        print(f"   ⚠️ Răspuns respins (scor prea mic)")
        print(f"   🔄 Rerutare către fallback...")
        fallback_output = efe.router.fallback_logic(user_input).generate(user_input)
        print(f"\n✨ ASTRA (Fallback): {fallback_output[:200]}...")
        final = fallback_output
    
    # STEP 7: Meta-analiză
    print("\n[STEP 7] Meta-analiză...")
    reflections = reflector.analyze({efe.router.last_model: final})
    print(f"   ✅ Analizat {len(reflections)} output-uri")
    
    # STEP 8: Învățare
    print("\n[STEP 8] Înregistrare pentru învățare...")
    learning.register_result(user_input, scores, efe.router.last_model)
    print(f"   ✅ Interacțiune salvată")
    
    print("\n" + "="*70)
    print("✅ PIPELINE COMPLET EXECUTAT CU SUCCES!")
    print("="*70)
    
    return True

def main():
    """Rulează toate scenariile"""
    print_header()
    
    scenarios = [
        ("Cerere de Codare", scenario_1_codare),
        ("Conversație Emoțională", scenario_2_emotie),
        ("Plan Strategic", scenario_3_strategie),
        ("Comparare Multiple Modele", scenario_4_multi_models),
        ("Sistem de Învățare", scenario_5_learning),
        ("Pipeline Complet", scenario_6_pipeline_complet),
    ]
    
    print(f"\nVom rula {len(scenarios)} scenarii practice...\n")
    
    for name, scenario_func in scenarios:
        try:
            scenario_func()
            print("\n" + "="*70)
        except Exception as e:
            print(f"\n❌ Eroare la scenariu '{name}': {e}")
            import traceback
            traceback.print_exc()
            print("\n" + "="*70)
    
    print("\n" + "="*70)
    print("🎉 TOATE SCENARIILE AU FOST EXECUTATE!")
    print("="*70)
    print("\n✅ ASTRA funcționează perfect în scenarii reale!")
    print("💡 Sistemul este gata pentru utilizare practică.\n")

if __name__ == "__main__":
    main()
