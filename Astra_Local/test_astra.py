#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 Test Script pentru ASTRA - Testare rapidă a funcționalităților
"""

import sys
from pathlib import Path

# Adăugă path-ul de bază
BASE_PATH = Path(__file__).parent
sys.path.insert(0, str(BASE_PATH))

def test_imports():
    """Testează importurile"""
    print("[TEST] Testare importuri...")
    try:
        from core_router.routing_manager import RoutingManager
        print("   [OK] RoutingManager")
        
        from scoring_module import ScoringModule
        print("   [OK] ScoringModule")
        
        from nexus_efe_core_engine import NexusEFE
        print("   [OK] NexusEFE")
        
        from meta_layer.coherence_validator import CoherenceValidator
        print("   [OK] CoherenceValidator")
        
        from meta_layer.meta_reflector import MetaReflector
        print("   [OK] MetaReflector")
        
        from Astrax2_Learning_Core import Astrax2Learning
        print("   [OK] Astrax2Learning")
        
        from Astrax2_LLM_Engine import Astrax2Engine
        print("   [OK] Astrax2Engine")
        
        print("\n[SUCCESS] Toate importurile functioneaza!\n")
        return True
    except ImportError as e:
        print(f"\n[ERROR] Eroare la import: {e}\n")
        return False

def test_routing():
    """Testează routing-ul"""
    print("[TEST] Testare Routing Manager...")
    try:
        from core_router.routing_manager import RoutingManager
        from llm_modules.mistral import MistralLLM
        from llm_modules.qwen import QwenLLM
        
        llm_pool = {
            "mistral": MistralLLM(),
            "qwen": QwenLLM(),
            "default": MistralLLM()
        }
        
        router = RoutingManager(llm_pool)
        
        # Test 1: Detectare cod
        test1 = router.direct_to_llm("Scrie-mi o funcție Python")
        print(f"   Test cod: {router.last_model}")
        
        # Test 2: Detectare emoție
        test2 = router.direct_to_llm("Simt dor de tine")
        print(f"   Test emoție: {router.last_model}")
        
        # Test 3: Detectare strategie
        test3 = router.direct_to_llm("Fă-mi un plan de MVP")
        print(f"   Test strategie: {router.last_model}")
        
        print("[SUCCESS] Routing functioneaza!\n")
        return True
    except Exception as e:
        print(f"[ERROR] Eroare routing: {e}\n")
        return False

def test_scoring():
    """Testează scoring-ul"""
    print("[TEST] Testare Scoring Module...")
    try:
        from scoring_module import ScoringModule
        
        scorer = ScoringModule()
        
        test_outputs = [
            "Aceasta este o analiză logică pentru că necesită o abordare structurată și rațională.",
            "Simt o undă de emoție care mă face să reflect asupra adâncurilor sufletului tău.",
            "Costul proiectului este de 5000€ cu un ROI estimat la 15% în primul an."
        ]
        
        for i, output in enumerate(test_outputs, 1):
            scores = scorer.evaluate_all(output)
            print(f"   Test {i}: Logic={scores['logic']:.2f}, Emotion={scores['emotion']:.2f}, Finance={scores['finance']:.2f}, Total={scores['total']:.2f}")
        
        print("[SUCCESS] Scoring functioneaza!\n")
        return True
    except Exception as e:
        print(f"[ERROR] Eroare scoring: {e}\n")
        return False

def test_efe_engine():
    """Testează EFE Engine"""
    print("[TEST] Testare EFE Core Engine...")
    try:
        from nexus_efe_core_engine import NexusEFE
        from llm_modules.mistral import MistralLLM
        from llm_modules.qwen import QwenLLM
        
        llm_pool = {
            "mistral": MistralLLM(),
            "qwen": QwenLLM(),
            "default": MistralLLM(),
            "backup": QwenLLM()
        }
        
        config = {
            "thresholds": {
                "accept": 0.75
            }
        }
        
        efe = NexusEFE(config, llm_pool)
        
        # Test procesare
        result = efe.process("Salut, cum ești?")
        print(f"   Răspuns generat: {result[:100]}...")
        
        print("[SUCCESS] EFE Engine functioneaza!\n")
        return True
    except Exception as e:
        print(f"[ERROR] Eroare EFE: {e}\n")
        import traceback
        traceback.print_exc()
        return False

def test_learning():
    """Testează sistemul de învățare"""
    print("[TEST] Testare AstraX2 Learning...")
    try:
        from Astrax2_Learning_Core import Astrax2Learning
        
        learning = Astrax2Learning()
        
        # Test înregistrare
        learning.register_result(
            "Test task",
            {"logic": 0.8, "emotion": 0.7, "finance": 0.6, "total": 0.7},
            "mistral"
        )
        
        # Test analiză tendințe
        trends = learning.analyze_trends()
        print(f"   Tendințe: {trends}")
        
        print("[SUCCESS] Learning functioneaza!\n")
        return True
    except Exception as e:
        print(f"[ERROR] Eroare learning: {e}\n")
        return False

def main():
    """Rulează toate testele"""
    # Setare encoding pentru Windows
    import sys
    import io
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("\n" + "="*60)
    print("TESTARE ASTRA - Verificare Functionalitati")
    print("="*60 + "\n")
    
    tests = [
        ("Importuri", test_imports),
        ("Routing", test_routing),
        ("Scoring", test_scoring),
        ("EFE Engine", test_efe_engine),
        ("Learning", test_learning)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"[ERROR] Eroare la test {name}: {e}\n")
            results.append((name, False))
    
    # Sumar
    print("="*60)
    print("REZULTATE TESTE:")
    print("="*60)
    
    for name, result in results:
        status = "[PASS]" if result else "[FAIL]"
        print(f"   {status} - {name}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\nRezultat: {passed}/{total} teste trecute")
    
    if passed == total:
        print("\n[SUCCESS] TOATE TESTELE AU TRECUT! ASTRA este functional!")
    else:
        print(f"\n[WARNING] {total - passed} teste au esuat. Verifica erorile de mai sus.")
    
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
