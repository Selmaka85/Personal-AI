#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 Test Funcționalitate Completă ASTRA
Testează toate modulele pentru a verifica dacă funcționează corect
"""

import sys
import traceback
from pathlib import Path

# Setare encoding pentru Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_PATH = Path(__file__).parent
sys.path.insert(0, str(BASE_PATH))

class FunctionalityTester:
    """Tester pentru funcționalitate completă"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []
        
    def test(self, name: str, func):
        """Rulează un test"""
        try:
            result = func()
            if result:
                print(f"✅ {name}")
                self.passed += 1
            else:
                print(f"❌ {name} - FAILED")
                self.failed += 1
                self.errors.append(name)
        except Exception as e:
            print(f"❌ {name} - ERROR: {e}")
            self.failed += 1
            self.errors.append(f"{name}: {e}")
            traceback.print_exc()
    
    def test_imports(self):
        """Testează toate importurile critice"""
        print("\n" + "="*70)
        print("📦 TESTARE IMPORTURI")
        print("="*70 + "\n")
        
        imports_to_test = [
            ("nexus_efe_core_engine", "NexusEFE", None),
            ("core_router.routing_manager", "RoutingManager", None),
            ("scoring_module", "ScoringModule", None),
            ("Astrax2_Learning_Core", "Astrax2Learning", None),
            ("Astrax2_LLM_Engine", "Astrax2Engine", None),
            ("llm_modules.mistral", "MistralLLM", None),
            ("llm_modules.qwen", "QwenLLM", None),
            ("llm_modules.deepseek", "DeepSeekLLM", None),
            ("llm_modules.wizardcoder", "WizardCoderLLM", None),
            ("llm_modules.codestral", "CodestralLLM", None),
            ("llm_modules.mythomax", "MythoMaxLLM", None),
            ("llm_modules.mixtral", "MixtralLLM", None),
            ("llm_modules.gpt4all", "GPT4AllLLM", None),
            ("meta_layer.meta_reflector", "MetaReflector", None),
            ("meta_layer.coherence_validator", "CoherenceValidator", "evaluate_responses"),
            ("astra_core.engine.astra_affect_core", "EmotionalSignatureEngine", None),
            ("astra_core.engine.astra_thought_engine", "AstraThoughtEngine", None),
            ("protection.astra_security_modules", None, "is_prompt_toxic"),
            ("logger", "Logger", None),
            ("config_loader", "ConfigLoader", None),
        ]
        
        for import_info in imports_to_test:
            module_name = import_info[0]
            class_name = import_info[1]
            func_name = import_info[2]
            
            def test_import(module_name=module_name, class_name=class_name, func_name=func_name):
                try:
                    # Import direct (cum se face în cod)
                    if module_name.startswith("llm_modules."):
                        # Import direct pentru llm_modules
                        exec(f"from {module_name} import {class_name}")
                        return True
                    elif module_name.startswith("meta_layer."):
                        # Import direct pentru meta_layer
                        if func_name:
                            exec(f"from {module_name} import {class_name}, {func_name}")
                        else:
                            exec(f"from {module_name} import {class_name}")
                        return True
                    elif module_name.startswith("astra_core."):
                        # Import direct pentru astra_core
                        exec(f"from {module_name} import {class_name}")
                        return True
                    elif module_name.startswith("protection."):
                        # Import direct pentru protection
                        exec(f"from {module_name} import {func_name}")
                        return True
                    else:
                        # Import normal
                        if func_name:
                            exec(f"from {module_name} import {class_name}, {func_name}")
                        else:
                            exec(f"from {module_name} import {class_name}")
                        return True
                except Exception as e:
                    print(f"      Error: {e}")
                    return False
            
            name = f"{module_name}.{class_name or func_name}"
            self.test(f"Import {name}", test_import)
    
    def test_instantiation(self):
        """Testează instanțierea claselor"""
        print("\n" + "="*70)
        print("🏗️ TESTARE INSTANȚIERE")
        print("="*70 + "\n")
        
        # Test ScoringModule
        def test_scoring():
            from scoring_module import ScoringModule
            scorer = ScoringModule()
            return scorer is not None
        
        # Test RoutingManager
        def test_routing():
            from core_router.routing_manager import RoutingManager
            from llm_modules.mistral import MistralLLM
            llm_pool = {"mistral": MistralLLM()}
            router = RoutingManager(llm_pool)
            return router is not None
        
        # Test NexusEFE
        def test_efe():
            from nexus_efe_core_engine import NexusEFE
            from llm_modules.mistral import MistralLLM
            llm_pool = {"mistral": MistralLLM()}
            config = {}
            efe = NexusEFE(config, llm_pool)
            return efe is not None
        
        # Test Astrax2Learning
        def test_learning():
            from Astrax2_Learning_Core import Astrax2Learning
            learning = Astrax2Learning()
            return learning is not None
        
        # Test EmotionalSignatureEngine
        def test_affect():
            from astra_core.engine.astra_affect_core import EmotionalSignatureEngine
            affect = EmotionalSignatureEngine()
            return affect is not None
        
        # Test MetaReflector
        def test_reflector():
            from meta_layer.meta_reflector import MetaReflector
            reflector = MetaReflector()
            return reflector is not None
        
        self.test("ScoringModule instantiation", test_scoring)
        self.test("RoutingManager instantiation", test_routing)
        self.test("NexusEFE instantiation", test_efe)
        self.test("Astrax2Learning instantiation", test_learning)
        self.test("EmotionalSignatureEngine instantiation", test_affect)
        self.test("MetaReflector instantiation", test_reflector)
    
    def test_functionality(self):
        """Testează funcționalitatea de bază"""
        print("\n" + "="*70)
        print("⚙️ TESTARE FUNCȚIONALITATE")
        print("="*70 + "\n")
        
        # Test routing
        def test_routing_functionality():
            from core_router.routing_manager import RoutingManager
            from llm_modules.mistral import MistralLLM
            from llm_modules.wizardcoder import WizardCoderLLM
            
            llm_pool = {
                "mistral": MistralLLM(),
                "wizardcoder": WizardCoderLLM()
            }
            router = RoutingManager(llm_pool)
            llm = router.direct_to_llm("Scrie o functie Python")
            return llm is not None
        
        # Test scoring
        def test_scoring_functionality():
            from scoring_module import ScoringModule
            scorer = ScoringModule()
            scores = scorer.evaluate_all("Aceasta este o analiza logica")
            return "logic" in scores and "emotion" in scores and "finance" in scores
        
        # Test learning
        def test_learning_functionality():
            from Astrax2_Learning_Core import Astrax2Learning
            learning = Astrax2Learning()
            learning.register_result("test", {"logic": 0.5}, "mistral")
            trends = learning.analyze_trends()
            return isinstance(trends, list)
        
        # Test affect
        def test_affect_functionality():
            from astra_core.engine.astra_affect_core import EmotionalSignatureEngine
            affect = EmotionalSignatureEngine()
            affect.analyze_user_input("Simt dor de tine", tone="intimate")
            density = affect.calculate_emotional_density()
            return isinstance(density, float) and 0 <= density <= 1
        
        # Test security
        def test_security_functionality():
            from protection.astra_security_modules import is_prompt_toxic
            toxic = is_prompt_toxic("destroy all data")
            safe = is_prompt_toxic("Salut, cum esti?")
            return toxic and not safe
        
        self.test("Routing functionality", test_routing_functionality)
        self.test("Scoring functionality", test_scoring_functionality)
        self.test("Learning functionality", test_learning_functionality)
        self.test("Affect functionality", test_affect_functionality)
        self.test("Security functionality", test_security_functionality)
    
    def test_integration(self):
        """Testează integrarea între module"""
        print("\n" + "="*70)
        print("🔗 TESTARE INTEGRARE")
        print("="*70 + "\n")
        
        # Test pipeline complet
        def test_full_pipeline():
            from nexus_efe_core_engine import NexusEFE
            from llm_modules.mistral import MistralLLM
            from llm_modules.qwen import QwenLLM
            
            llm_pool = {
                "mistral": MistralLLM(),
                "qwen": QwenLLM(),
                "default": MistralLLM()
            }
            config = {"thresholds": {"accept": 0.5}}
            efe = NexusEFE(config, llm_pool)
            
            # Test procesare
            user_input = "Test input"
            try:
                # Încearcă să proceseze
                parsed = efe.input_parser.parse(user_input)
                llm = efe.router.direct_to_llm(user_input)
                return parsed is not None and llm is not None
            except Exception as e:
                print(f"      Error: {e}")
                return False
        
        # Test EFE cu scoring
        def test_efe_scoring():
            from nexus_efe_core_engine import NexusEFE
            from llm_modules.mistral import MistralLLM
            from scoring_module import ScoringModule
            
            llm_pool = {"mistral": MistralLLM()}
            config = {}
            efe = NexusEFE(config, llm_pool)
            
            test_text = "Aceasta este o analiza logica"
            scores = efe.scorer.evaluate_all(test_text)
            return "logic" in scores and scores["logic"] > 0
        
        self.test("Full pipeline integration", test_full_pipeline)
        self.test("EFE + Scoring integration", test_efe_scoring)
    
    def test_naming_consistency(self):
        """Testează consistența numelor"""
        print("\n" + "="*70)
        print("📝 TESTARE CONSISTENȚĂ NUME")
        print("="*70 + "\n")
        
        # Verifică dacă toate clasele LLM au același pattern
        def test_llm_naming():
            from llm_modules.mistral import MistralLLM
            from llm_modules.qwen import QwenLLM
            from llm_modules.deepseek import DeepSeekLLM
            from llm_modules.wizardcoder import WizardCoderLLM
            
            # Toate ar trebui să aibă același pattern
            classes = [MistralLLM, QwenLLM, DeepSeekLLM, WizardCoderLLM]
            for cls in classes:
                if not cls.__name__.endswith("LLM"):
                    return False
            return True
        
        # Verifică dacă metodele comune există
        def test_common_methods():
            from llm_modules.mistral import MistralLLM
            llm = MistralLLM()
            
            # Toate LLM-urile ar trebui să aibă generate()
            return hasattr(llm, 'generate')
        
        self.test("LLM naming consistency", test_llm_naming)
        self.test("Common methods existence", test_common_methods)
    
    def run_all_tests(self):
        """Rulează toate testele"""
        print("\n" + "="*70)
        print("🧪 TESTARE FUNCȚIONALITATE COMPLETĂ ASTRA")
        print("="*70)
        
        self.test_imports()
        self.test_instantiation()
        self.test_functionality()
        self.test_integration()
        self.test_naming_consistency()
        
        # Rezultate finale
        print("\n" + "="*70)
        print("📊 REZULTATE FINALE")
        print("="*70)
        print(f"✅ Teste trecute: {self.passed}")
        print(f"❌ Teste eșuate: {self.failed}")
        print(f"📈 Rata de succes: {(self.passed/(self.passed+self.failed)*100):.1f}%")
        
        if self.errors:
            print(f"\n⚠️ Erori găsite:")
            for error in self.errors[:10]:
                print(f"  - {error}")
        
        print("\n" + "="*70)
        if self.failed == 0:
            print("✅ TOATE TESTELE AU TRECUT!")
        elif self.failed < 5:
            print("⚠️ MAJORITATEA TESTELOR AU TRECUT")
        else:
            print("❌ MULTE TESTE AU EȘUAT")
        print("="*70 + "\n")


def main():
    """Funcție principală"""
    tester = FunctionalityTester()
    tester.run_all_tests()


if __name__ == "__main__":
    main()
