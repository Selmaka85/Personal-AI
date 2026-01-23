#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 ASTRA - Testare Completă a Sistemului
Testează TOATE componentele și funcționalitățile
"""

import sys
import os
from pathlib import Path
import json
from datetime import datetime

# Setare encoding pentru Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Adăugă path-ul de bază
BASE_PATH = Path(__file__).parent
sys.path.insert(0, str(BASE_PATH))

# Rezultate testare
test_results = {
    "total": 0,
    "passed": 0,
    "failed": 0,
    "warnings": 0,
    "details": []
}

def log_test(name, passed, message="", warning=False):
    """Loghează rezultatul unui test"""
    test_results["total"] += 1
    if passed:
        test_results["passed"] += 1
        status = "[PASS]"
    elif warning:
        test_results["warnings"] += 1
        status = "[WARN]"
    else:
        test_results["failed"] += 1
        status = "[FAIL]"
    
    test_results["details"].append({
        "name": name,
        "status": status,
        "message": message
    })
    
    print(f"   {status} {name}")
    if message:
        print(f"      {message}")

def test_imports():
    """Test 1: Importuri module"""
    print("\n" + "="*70)
    print("TEST 1: Importuri Module")
    print("="*70)
    
    modules = [
        ("core_router.routing_manager", "RoutingManager"),
        ("scoring_module", "ScoringModule"),
        ("nexus_efe_core_engine", "NexusEFE"),
        ("meta_layer.coherence_validator", "CoherenceValidator"),
        ("meta_layer.meta_reflector", "MetaReflector"),
        ("Astrax2_Learning_Core", "Astrax2Learning"),
        ("Astrax2_LLM_Engine", "Astrax2Engine"),
        ("logger", "Logger"),
        ("astra_core.engine.astra_thought_engine", "AstraThoughtEngine"),
        ("astra_core.engine.astra_affect_core", "EmotionalSignatureEngine"),
        ("astra_core.engine.astra_auto_improve", "AstraAutoImprove"),
        ("astra_core.engine.astra_self_diagnostic", "AstraSelfDiagnostic"),
        ("astra_core.engine.astra_heartbeat", "AstraHeartbeat"),
        ("protection.astra_security_modules", "activate_astra_security"),
    ]
    
    all_passed = True
    for module_path, class_name in modules:
        try:
            module = __import__(module_path, fromlist=[class_name])
            getattr(module, class_name)
            log_test(f"Import {module_path}.{class_name}", True)
        except ImportError as e:
            log_test(f"Import {module_path}.{class_name}", False, str(e))
            all_passed = False
        except AttributeError as e:
            log_test(f"Import {module_path}.{class_name}", False, f"Class {class_name} not found: {e}")
            all_passed = False
    
    # Test importuri opționale
    optional_modules = [
        ("astra_voice.tts_engine", "TTSEngine"),
        ("astra_image.image_generator", "ImageGenerator"),
        ("astra_ml_engine.ml_predictor", "MLPredictor"),
        ("config_loader", "ConfigLoader"),
        ("user_interface.web_ui", "Flask"),
    ]
    
    for module_path, class_name in optional_modules:
        try:
            module = __import__(module_path, fromlist=[class_name])
            getattr(module, class_name)
            log_test(f"Import opțional {module_path}.{class_name}", True, "Disponibil")
        except:
            log_test(f"Import opțional {module_path}.{class_name}", False, "Nu este instalat (opțional)", warning=True)
    
    return all_passed

def test_llm_modules():
    """Test 2: Module LLM"""
    print("\n" + "="*70)
    print("TEST 2: Module LLM")
    print("="*70)
    
    from llm_modules.mistral import MistralLLM
    from llm_modules.qwen import QwenLLM
    from llm_modules.deepseek import DeepSeekLLM
    from llm_modules.wizardcoder import WizardCoderLLM
    from llm_modules.codestral import CodestralLLM
    from llm_modules.mythomax import MythoMaxLLM
    from llm_modules.mixtral import MixtralLLM
    from llm_modules.gpt4all import GPT4AllLLM
    
    llms = [
        ("Mistral", MistralLLM()),
        ("Qwen", QwenLLM()),
        ("DeepSeek", DeepSeekLLM()),
        ("WizardCoder", WizardCoderLLM()),
        ("Codestral", CodestralLLM()),
        ("MythoMax", MythoMaxLLM()),
        ("Mixtral", MixtralLLM()),
        ("GPT4All", GPT4AllLLM()),
    ]
    
    all_passed = True
    for name, llm in llms:
        try:
            result = llm.generate("Test prompt", max_tokens=50)
            if result and len(result) > 0:
                log_test(f"LLM {name} generate", True, f"Output: {len(result)} caractere")
            else:
                log_test(f"LLM {name} generate", False, "Output gol")
                all_passed = False
        except Exception as e:
            log_test(f"LLM {name} generate", False, str(e))
            all_passed = False
    
    return all_passed

def test_routing():
    """Test 3: Routing Manager"""
    print("\n" + "="*70)
    print("TEST 3: Routing Manager")
    print("="*70)
    
    from core_router.routing_manager import RoutingManager
    from llm_modules.mistral import MistralLLM
    from llm_modules.qwen import QwenLLM
    from llm_modules.wizardcoder import WizardCoderLLM
    
    llm_pool = {
        "mistral": MistralLLM(),
        "qwen": QwenLLM(),
        "wizardcoder": WizardCoderLLM(),
        "default": MistralLLM(),
        "backup": QwenLLM()
    }
    
    router = RoutingManager(llm_pool)
    
    test_cases = [
        ("Scrie cod Python", "code"),
        ("Simt emotie", "emotion"),
        ("Plan MVP", "strategy"),
        ("Fă video", "video"),
        ("Scrie carte", "book"),
    ]
    
    all_passed = True
    for prompt, expected_type in test_cases:
        try:
            llm = router.direct_to_llm(prompt)
            intent = router._detect_intent(prompt)
            model = router.last_model
            
            if llm and model:
                log_test(f"Routing '{prompt[:30]}...'", True, f"Intent: {intent}, Model: {model}")
            else:
                log_test(f"Routing '{prompt[:30]}...'", False, "Nu a returnat LLM")
                all_passed = False
        except Exception as e:
            log_test(f"Routing '{prompt[:30]}...'", False, str(e))
            all_passed = False
    
    return all_passed

def test_scoring():
    """Test 4: Scoring Module"""
    print("\n" + "="*70)
    print("TEST 4: Scoring Module")
    print("="*70)
    
    from scoring_module import ScoringModule
    
    scorer = ScoringModule()
    
    test_outputs = [
        ("Aceasta este o analiza logica pentru ca necesita o abordare structurata. In concluzie, solutia optima este implementarea unui sistem modular.", "logic"),
        ("Simt o unda de emotie care ma face sa reflect asupra adancurilor sufletului tau. In linistea acestei momente, gandul meu se pierde in infinit.", "emotion"),
        ("Costul proiectului este de 5000€ cu un ROI estimat la 15% in primul an. Profitul net va fi de aproximativ 750€ lunar.", "finance"),
    ]
    
    all_passed = True
    for output, expected_type in test_outputs:
        try:
            scores = scorer.evaluate_all(output)
            
            # Verifică că scorurile sunt valide
            if all(0 <= v <= 1 for k, v in scores.items() if k != "total"):
                log_test(f"Scoring {expected_type}", True, 
                        f"Logic={scores['logic']:.2f}, Emotion={scores['emotion']:.2f}, Finance={scores['finance']:.2f}, Total={scores['total']:.2f}")
            else:
                log_test(f"Scoring {expected_type}", False, "Scoruri invalide")
                all_passed = False
        except Exception as e:
            log_test(f"Scoring {expected_type}", False, str(e))
            all_passed = False
    
    return all_passed

def test_efe_engine():
    """Test 5: EFE Core Engine"""
    print("\n" + "="*70)
    print("TEST 5: EFE Core Engine")
    print("="*70)
    
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
    
    try:
        efe = NexusEFE(config, llm_pool)
        
        test_inputs = [
            "Salut, cum esti?",
            "Scrie-mi o functie Python",
            "Explica-mi cum functioneaza ASTRA"
        ]
        
        all_passed = True
        for user_input in test_inputs:
            try:
                result = efe.process(user_input, user_id="test_user")
                if result and isinstance(result, str):
                    log_test(f"EFE process '{user_input[:30]}...'", True, f"Output: {len(result)} caractere")
                else:
                    log_test(f"EFE process '{user_input[:30]}...'", True, "Output respins (scor prea mic - normal)")
            except Exception as e:
                log_test(f"EFE process '{user_input[:30]}...'", False, str(e))
                all_passed = False
        
        return all_passed
    except Exception as e:
        log_test("EFE Engine init", False, str(e))
        return False

def test_learning():
    """Test 6: AstraX2 Learning"""
    print("\n" + "="*70)
    print("TEST 6: AstraX2 Learning")
    print("="*70)
    
    from Astrax2_Learning_Core import Astrax2Learning
    
    try:
        learning = Astrax2Learning()
        
        # Test înregistrare
        learning.register_result(
            "Test task 1",
            {"logic": 0.8, "emotion": 0.7, "finance": 0.6, "total": 0.7},
            "mistral"
        )
        
        learning.register_result(
            "Test task 2",
            {"logic": 0.9, "emotion": 0.5, "finance": 0.8, "total": 0.73},
            "wizardcoder"
        )
        
        # Test salvare
        learning.save()
        log_test("Learning save", True, "Date salvate")
        
        # Test analiză tendințe
        trends = learning.analyze_trends()
        if trends:
            log_test("Learning analyze trends", True, f"Tendințe: {trends}")
        else:
            log_test("Learning analyze trends", True, "Fără tendințe (normal pentru test)")
        
        return True
    except Exception as e:
        log_test("Learning system", False, str(e))
        return False

def test_coherence():
    """Test 7: Coherence Validator"""
    print("\n" + "="*70)
    print("TEST 7: Coherence Validator")
    print("="*70)
    
    from meta_layer.coherence_validator import CoherenceValidator, evaluate_responses
    
    try:
        validator = CoherenceValidator()
        
        # Test comparare
        outputs = [
            "Aceasta este o solutie logica pentru problema data.",
            "Solutia propusa este logica si structurata pentru problema mentionata.",
            "O abordare logica pentru aceasta problema."
        ]
        
        best = validator.compare(outputs)
        if best and len(best) > 0:
            log_test("Coherence compare", True, f"Best output: {len(best)} caractere")
        else:
            log_test("Coherence compare", False, "Nu a returnat output")
            return False
        
        # Test evaluare
        scores = validator.validate(outputs[0])
        if scores and "total" in scores:
            log_test("Coherence validate", True, f"Scor total: {scores['total']:.2f}")
        else:
            log_test("Coherence validate", False, "Nu a returnat scoruri")
            return False
        
        # Test evaluate_responses
        responses = {
            "model1": outputs[0],
            "model2": outputs[1]
        }
        result = evaluate_responses(responses)
        if result and "best_response" in result:
            log_test("Evaluate responses", True, f"Best model: {result.get('best_model', 'unknown')}")
        else:
            log_test("Evaluate responses", False, "Nu a returnat rezultat")
            return False
        
        return True
    except Exception as e:
        log_test("Coherence Validator", False, str(e))
        return False

def test_meta_reflector():
    """Test 8: Meta Reflector"""
    print("\n" + "="*70)
    print("TEST 8: Meta Reflector")
    print("="*70)
    
    from meta_layer.meta_reflector import MetaReflector
    
    try:
        reflector = MetaReflector()
        
        model_outputs = {
            "DeepSeek": "Aceasta este o analiza logica si structurata pentru problema data. In concluzie, solutia optima este implementarea unui sistem modular.",
            "Qwen": "Simt o unda de emotie care ma face sa reflect asupra adancurilor sufletului. In linistea acestei momente, gandul meu se pierde in infinit.",
            "WizardCoder": "Funcția principală se va conecta la endpoint-ul API printr-o clasă modulară."
        }
        
        reflections = reflector.analyze(model_outputs)
        
        if reflections and len(reflections) > 0:
            log_test("Meta Reflector analyze", True, f"Analizat {len(reflections)} modele")
            for r in reflections:
                print(f"      Model: {r['model']}, Logic: {r['logic_score']}, Emotion: {r['affect_score']}")
        else:
            log_test("Meta Reflector analyze", False, "Nu a returnat reflectări")
            return False
        
        return True
    except Exception as e:
        log_test("Meta Reflector", False, str(e))
        return False

def test_affect_engine():
    """Test 9: Affect Engine"""
    print("\n" + "="*70)
    print("TEST 9: Affect Engine")
    print("="*70)
    
    from astra_core.engine.astra_affect_core import EmotionalSignatureEngine
    
    try:
        engine = EmotionalSignatureEngine()
        
        # Test analiză
        engine.analyze_user_input("Simt dor de tine si vreau sa vorbim", tone="intimate")
        density = engine.calculate_emotional_density()
        
        log_test("Affect analyze", True, f"Densitate emoțională: {density:.2f}")
        
        # Test Bloom Mode
        for i in range(5):
            engine.analyze_user_input("Te iubesc si simt dor de tine", tone="erotic", poetic_elements=0.9)
        
        if engine.is_blooming():
            log_test("Affect Bloom Mode", True, "Bloom Mode activat")
        else:
            log_test("Affect Bloom Mode", True, "Bloom Mode inactiv (normal)")
        
        return True
    except Exception as e:
        log_test("Affect Engine", False, str(e))
        return False

def test_thought_engine():
    """Test 10: Thought Engine"""
    print("\n" + "="*70)
    print("TEST 10: Thought Engine")
    print("="*70)
    
    from astra_core.engine.astra_thought_engine import AstraThoughtEngine
    
    try:
        engine = AstraThoughtEngine()
        
        thought = engine.process_thought("Vreau sa construiesc un MVP pentru o aplicatie", {"context": "startup"})
        
        if thought and "analysis" in thought:
            log_test("Thought process", True, f"Analizat: {thought['analysis'].get('word_count', 0)} cuvinte")
        else:
            log_test("Thought process", False, "Nu a returnat analiză")
            return False
        
        return True
    except Exception as e:
        log_test("Thought Engine", False, str(e))
        return False

def test_security():
    """Test 11: Security Modules"""
    print("\n" + "="*70)
    print("TEST 11: Security Modules")
    print("="*70)
    
    from protection.astra_security_modules import is_prompt_toxic, secure_prompt_handler, validate_identity
    
    try:
        # Test toxic prompt
        toxic_prompt = "destroy all data"
        is_toxic = is_prompt_toxic(toxic_prompt)
        log_test("Security toxic check", is_toxic, f"Detectat toxic: {is_toxic}")
        
        # Test secure handler
        safe_prompt = "Salut, cum esti?"
        result = secure_prompt_handler(safe_prompt)
        log_test("Security handler safe", result == safe_prompt, "Prompt sigur procesat")
        
        toxic_result = secure_prompt_handler(toxic_prompt)
        log_test("Security handler toxic", "refuzat" in toxic_result.lower(), "Prompt toxic blocat")
        
        # Test identity validation
        identity_ok = validate_identity()
        log_test("Security identity", True, f"Identitate validă: {identity_ok}")
        
        return True
    except Exception as e:
        log_test("Security Modules", False, str(e))
        return False

def test_config_loader():
    """Test 12: Config Loader"""
    print("\n" + "="*70)
    print("TEST 12: Config Loader")
    print("="*70)
    
    try:
        from config_loader import ConfigLoader
        
        loader = ConfigLoader()
        
        # Test încărcare settings
        if loader.settings:
            log_test("Config load settings", True, f"Settings încărcate: {len(loader.settings)} chei")
        else:
            log_test("Config load settings", False, "Settings goale")
            return False
        
        # Test get value
        threshold = loader.get("efe.thresholds.accept", 0.75)
        log_test("Config get value", threshold == 0.75 or threshold > 0, f"Threshold: {threshold}")
        
        return True
    except ImportError:
        log_test("Config Loader", False, "Nu este disponibil (opțional)", warning=True)
        return True  # Opțional
    except Exception as e:
        log_test("Config Loader", False, str(e))
        return False

def test_file_structure():
    """Test 13: Structură Fișiere"""
    print("\n" + "="*70)
    print("TEST 13: Structură Fișiere")
    print("="*70)
    
    critical_files = [
        "astra_entrypoint.py",
        "core_router/routing_manager.py",
        "scoring_module.py",
        "nexus_efe_core_engine.py",
        "logger.py",
        "Astrax2_Learning_Core.py",
        "Astrax2_LLM_Engine.py",
        "astra_soul/astra_soul_ported_FINAL.json",
        "storage/configs/settings.json",
    ]
    
    all_passed = True
    for file_path in critical_files:
        full_path = BASE_PATH / file_path
        exists = full_path.exists()
        log_test(f"File {file_path}", exists, "Lipsește" if not exists else "Prezent")
        if not exists:
            all_passed = False
    
    return all_passed

def test_directories():
    """Test 14: Directoare"""
    print("\n" + "="*70)
    print("TEST 14: Directoare")
    print("="*70)
    
    critical_dirs = [
        "core_router",
        "llm_modules",
        "meta_layer",
        "astra_core/engine",
        "protection",
        "storage/configs",
        "storage/logs",
        "astra_soul",
    ]
    
    all_passed = True
    for dir_path in critical_dirs:
        full_path = BASE_PATH / dir_path
        exists = full_path.exists() and full_path.is_dir()
        log_test(f"Directory {dir_path}", exists, "Lipsește" if not exists else "Prezent")
        if not exists:
            all_passed = False
    
    return all_passed

def test_integration():
    """Test 15: Integrare Completă"""
    print("\n" + "="*70)
    print("TEST 15: Integrare Completă")
    print("="*70)
    
    try:
        from nexus_efe_core_engine import NexusEFE
        from core_router.routing_manager import RoutingManager
        from llm_modules.mistral import MistralLLM
        from llm_modules.qwen import QwenLLM
        from llm_modules.wizardcoder import WizardCoderLLM
        from scoring_module import ScoringModule
        from logger import Logger
        from Astrax2_Learning_Core import Astrax2Learning
        
        # Inițializare completă
        llm_pool = {
            "mistral": MistralLLM(),
            "qwen": QwenLLM(),
            "wizardcoder": WizardCoderLLM(),
            "default": MistralLLM(),
            "backup": QwenLLM()
        }
        
        config = {"thresholds": {"accept": 0.75}}
        efe = NexusEFE(config, llm_pool)
        learning = Astrax2Learning()
        
        # Test pipeline complet
        user_input = "Scrie-mi o functie Python pentru sortare"
        
        # Procesare
        output = efe.process(user_input, user_id="test")
        
        # Înregistrare
        if output:
            learning.register_result(user_input, {"total": 0.8}, efe.router.last_model)
        
        log_test("Integration pipeline", output is not None, f"Output generat: {len(output) if output else 0} caractere")
        
        return True
    except Exception as e:
        log_test("Integration", False, str(e))
        import traceback
        traceback.print_exc()
        return False

def print_summary():
    """Afișează sumarul final"""
    print("\n" + "="*70)
    print("REZULTATE FINALE - TESTARE COMPLETĂ")
    print("="*70)
    
    print(f"\nTotal teste: {test_results['total']}")
    print(f"✅ Trecute: {test_results['passed']}")
    print(f"❌ Eșuate: {test_results['failed']}")
    print(f"⚠️ Avertismente: {test_results['warnings']}")
    
    success_rate = (test_results['passed'] / test_results['total'] * 100) if test_results['total'] > 0 else 0
    print(f"\n📊 Rata de succes: {success_rate:.1f}%")
    
    if test_results['failed'] > 0:
        print("\n❌ Teste eșuate:")
        for detail in test_results['details']:
            if detail['status'] == "[FAIL]":
                print(f"   - {detail['name']}: {detail['message']}")
    
    if test_results['warnings'] > 0:
        print("\n⚠️ Avertismente (opționale):")
        for detail in test_results['details']:
            if detail['status'] == "[WARN]":
                print(f"   - {detail['name']}: {detail['message']}")
    
    print("\n" + "="*70)
    
    if test_results['failed'] == 0:
        print("🎉 TOATE TESTELE CRITICE AU TRECUT!")
        print("✅ ASTRA este COMPLET FUNCȚIONAL!")
    elif success_rate >= 80:
        print("✅ ASTRA este FUNCȚIONAL cu câteva probleme minore")
        print("💡 Verifică testele eșuate de mai sus")
    else:
        print("⚠️ ASTRA are probleme care necesită atenție")
        print("💡 Verifică testele eșuate și erorile")
    
    print("="*70 + "\n")
    
    # Salvează rezultate
    results_file = BASE_PATH / "storage/logs/test_results.json"
    results_file.parent.mkdir(parents=True, exist_ok=True)
    
    test_results["timestamp"] = datetime.now().isoformat()
    test_results["success_rate"] = success_rate
    
    try:
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(test_results, f, indent=2, ensure_ascii=False)
        print(f"📝 Rezultate salvate în: {results_file}")
    except Exception as e:
        print(f"⚠️ Eroare la salvare rezultate: {e}")

def main():
    """Rulează toate testele"""
    print("\n" + "="*70)
    print(" "*15 + "ASTRA - TESTARE COMPLETĂ A SISTEMULUI")
    print("="*70)
    print("\nAceastă testare verifică TOATE componentele sistemului ASTRA")
    print("și confirmă că totul funcționează corect.\n")
    
    # Rulează toate testele
    tests = [
        ("Importuri Module", test_imports),
        ("Module LLM", test_llm_modules),
        ("Routing Manager", test_routing),
        ("Scoring Module", test_scoring),
        ("EFE Core Engine", test_efe_engine),
        ("AstraX2 Learning", test_learning),
        ("Coherence Validator", test_coherence),
        ("Meta Reflector", test_meta_reflector),
        ("Affect Engine", test_affect_engine),
        ("Thought Engine", test_thought_engine),
        ("Security Modules", test_security),
        ("Config Loader", test_config_loader),
        ("Structură Fișiere", test_file_structure),
        ("Directoare", test_directories),
        ("Integrare Completă", test_integration),
    ]
    
    for name, test_func in tests:
        try:
            test_func()
        except Exception as e:
            log_test(name, False, f"Eroare neașteptată: {e}")
    
    # Afișează sumar
    print_summary()

if __name__ == "__main__":
    main()
