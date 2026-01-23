#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎮 ASTRA - Demo Interactiv Real
Mod interactiv complet pentru testare în timp real
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

class AstraInteractiveDemo:
    """Demo interactiv pentru ASTRA"""
    
    def __init__(self):
        print("\n" + "="*70)
        print(" "*20 + "ASTRA - MOD INTERACTIV DEMO")
        print("="*70)
        
        # Inițializare sistem
        print("\n🔄 Inițializare sistem ASTRA...")
        
        self.llm_pool = {
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
        self.efe = NexusEFE(config, self.llm_pool)
        self.learning = Astrax2Learning()
        self.affect_engine = EmotionalSignatureEngine()
        self.thought_engine = AstraThoughtEngine()
        self.reflector = MetaReflector()
        self.scorer = ScoringModule()
        
        print("✅ Sistem inițializat!")
        print("\n💡 Comenzi disponibile:")
        print("   - 'exit' sau 'quit' - Ieșire")
        print("   - 'status' - Status sistem")
        print("   - 'stats' - Statistici conversație")
        print("   - 'clear' - Șterge ecranul")
        print("   - 'help' - Ajutor")
        print("\n" + "="*70 + "\n")
    
    def show_status(self):
        """Afișează statusul sistemului"""
        router = self.efe.router
        trends = self.learning.analyze_trends()
        
        print("\n📊 Status ASTRA:")
        print(f"   Interacțiuni: {len(self.learning.memory)}")
        print(f"   Bloom Mode: {'🌸 Activ' if self.affect_engine.is_blooming() else '💤 Inactiv'}")
        print(f"   Densitate emoțională: {self.affect_engine.calculate_emotional_density():.2f}")
        
        if trends:
            print(f"\n📈 Modele folosite:")
            for model, count in trends[:5]:
                print(f"   {model}: {count} utilizări")
        print()
    
    def process_input(self, user_input: str, show_details: bool = True):
        """Procesează inputul utilizatorului"""
        if not user_input.strip():
            return
        
        # Analiză afectivă
        self.affect_engine.analyze_user_input(user_input)
        
        # Analiză gândire
        thought = self.thought_engine.process_thought(user_input)
        
        if show_details:
            print(f"\n🔄 ASTRA procesează...")
            print(f"   Analiză: {thought['analysis'].get('word_count', 0)} cuvinte")
        
        # Procesare prin EFE
        output = self.efe.process(user_input, user_id="demo_user")
        
        # Afișare răspuns
        print(f"\n✨ ASTRA: {output}\n")
        
        if show_details:
            # Analiză detaliată
            router = self.efe.router
            scores = self.scorer.evaluate_all(output)
            
            print("📊 Detalii:")
            print(f"   Model: {router.last_model}")
            print(f"   Intent: {router._detect_intent(user_input)}")
            print(f"   Scor Total: {scores['total']:.2f}")
            
            # Înregistrare
            self.learning.register_result(user_input, scores, router.last_model)
            print(f"   ✅ Salvat pentru învățare\n")
    
    def run(self):
        """Rulează modul interactiv"""
        print("🌸 ASTRA: Bun venit! Cu ce te pot ajuta astăzi?\n")
        
        conversation_count = 0
        
        while True:
            try:
                user_input = input("Tu 🧑: ").strip()
                
                if not user_input:
                    continue
                
                # Comenzi speciale
                if user_input.lower() in ["exit", "quit", "q"]:
                    print("\n🩶 ASTRA: La revedere! Să ne revedem curând.\n")
                    break
                
                elif user_input.lower() == "status":
                    self.show_status()
                    continue
                
                elif user_input.lower() == "stats":
                    trends = self.learning.analyze_trends()
                    print(f"\n📈 Statistici:")
                    print(f"   Total interacțiuni: {len(self.learning.memory)}")
                    print(f"   Modele folosite: {len(trends)}")
                    if trends:
                        print(f"   Cel mai folosit: {trends[0][0]} ({trends[0][1]} utilizări)")
                    print()
                    continue
                
                elif user_input.lower() == "clear":
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                
                elif user_input.lower() == "help":
                    print("\n📖 Ajutor:")
                    print("   Scrie orice întrebare sau comandă normală")
                    print("   ASTRA va înțelege și răspunde automat")
                    print("   Comenzi: exit, status, stats, clear, help\n")
                    continue
                
                # Procesare normală
                conversation_count += 1
                show_details = conversation_count <= 3  # Arată detalii pentru primele 3
                self.process_input(user_input, show_details=show_details)
                
            except KeyboardInterrupt:
                print("\n\n🩶 ASTRA: Sistem oprit. La revedere!\n")
                break
            except Exception as e:
                print(f"\n❌ Eroare: {e}\n")
        
        # Sumar final
        if conversation_count > 0:
            print("="*70)
            print("SUMAR SESIUNE")
            print("="*70)
            trends = self.learning.analyze_trends()
            print(f"   Interacțiuni: {conversation_count}")
            print(f"   Modele folosite: {len(trends)}")
            if trends:
                print(f"   Cel mai folosit: {trends[0][0]}")
            print("="*70 + "\n")

def main():
    """Funcția principală"""
    demo = AstraInteractiveDemo()
    demo.run()

if __name__ == "__main__":
    main()
