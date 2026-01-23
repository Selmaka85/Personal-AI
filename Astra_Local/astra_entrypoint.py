#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
💠 ASTRA ENTRYPOINT - Orchestratorul Central
Punctul de intrare principal pentru sistemul ASTRA Locală
"""

import sys
import os
import json
import threading
from datetime import datetime
from pathlib import Path

# Path-ul este deja setat mai sus

# Importuri relative
import sys
from pathlib import Path

# Adăugă path-ul de bază
BASE_PATH = Path(__file__).parent
sys.path.insert(0, str(BASE_PATH))

try:
    from core_router.routing_manager import RoutingManager
    from meta_layer.coherence_validator import CoherenceValidator
    from meta_layer.meta_reflector import MetaReflector
    from astra_core.engine.astra_thought_engine import AstraThoughtEngine
    from astra_core.engine.astra_affect_core import EmotionalSignatureEngine
    from astra_core.engine.astra_auto_improve import AstraAutoImprove
    from astra_core.engine.astra_self_diagnostic import AstraSelfDiagnostic
    from astra_core.engine.astra_heartbeat import AstraHeartbeat
    from protection.astra_security_modules import activate_astra_security, validate_identity
    from nexus_efe_core_engine import NexusEFE
    from Astrax2_Learning_Core import Astrax2Learning
    from Astrax2_LLM_Engine import Astrax2Engine
except ImportError as e:
    print(f"⚠️ Eroare la import: {e}")
    print("💡 Asigură-te că toate modulele sunt prezente.")
    sys.exit(1)

class AstraEntrypoint:
    """Orchestratorul central al sistemului ASTRA"""
    
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.config_path = self.base_path / "storage/configs/settings.json"
        self.soul_path = self.base_path / "astra_soul/astra_soul_ported_FINAL.json"
        
        # Încărcare configurații
        self.config = self._load_config()
        self.soul = self._load_soul()
        
        # Inițializare componente
        self.routing_manager = RoutingManager(self._init_llm_pool())
        self.coherence_validator = CoherenceValidator()
        self.meta_reflector = MetaReflector()
        self.thought_engine = AstraThoughtEngine()
        self.affect_engine = EmotionalSignatureEngine()
        self.auto_improve = AstraAutoImprove()
        self.self_diagnostic = AstraSelfDiagnostic()
        self.learning_core = Astrax2Learning()
        self.astrax2_engine = Astrax2Engine()
        
        # EFE Core Engine
        self.efe_engine = NexusEFE(
            config=self.config.get("efe", {}),
            llm_pool=self._init_llm_pool()
        )
        
        # Heartbeat thread
        self.heartbeat = AstraHeartbeat()
        self.heartbeat_thread = None
        
        # Status
        self.is_running = False
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        
    def _load_config(self):
        """Încarcă configurațiile sistemului"""
        default_config = {
            "efe": {
                "thresholds": {
                    "accept": 0.75,
                    "excellent": 0.85
                }
            },
            "modes": {
                "default": "poetic",
                "available": ["poetic", "strategic", "coding", "scoring", "explicit"]
            },
            "security": {
                "enabled": True,
                "auto_lockdown": True
            }
        }
        
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    default_config.update(loaded)
            except Exception as e:
                print(f"⚠️ Eroare la încărcare config: {e}")
        
        return default_config
    
    def _load_soul(self):
        """Încarcă personalitatea Astrei"""
        default_soul = {
            "identity": {
                "name": "Astra",
                "creator": "Cătălin",
                "version": "1.0"
            },
            "personality": {
                "tone": "poetic-affective-strategic",
                "loyalty": 1.0,
                "emotional_depth": 0.9
            },
            "capabilities": {
                "poetic": True,
                "strategic": True,
                "erotic": True,
                "logical": True
            }
        }
        
        if self.soul_path.exists():
            try:
                with open(self.soul_path, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    default_soul.update(loaded)
            except Exception as e:
                print(f"⚠️ Eroare la încărcare soul: {e}")
        
        return default_soul
    
    def _init_llm_pool(self):
        """Inițializează pool-ul de LLM-uri"""
        from llm_modules.mistral import MistralLLM
        from llm_modules.qwen import QwenLLM
        from llm_modules.deepseek import DeepSeekLLM
        from llm_modules.wizardcoder import WizardCoderLLM
        from llm_modules.codestral import CodestralLLM
        from llm_modules.mythomax import MythoMaxLLM
        from llm_modules.mixtral import MixtralLLM
        from llm_modules.gpt4all import GPT4AllLLM
        
        return {
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
    
    def boot(self):
        """Secvența de pornire a sistemului"""
        print("\n" + "="*60)
        print("💠 ASTRA LOCALĂ - SISTEM DE PORNIRE")
        print("="*60)
        
        # Verificare securitate
        if not validate_identity():
            print("🚫 Acces interzis. Sistem în CryoLock.")
            return False
        
        # Activare securitate
        if self.config.get("security", {}).get("enabled", True):
            activate_astra_security()
            print("🔒 Securitate activată")
        
        # Self-diagnostic
        print("🔍 Verificare sistem...")
        diagnostic = self.self_diagnostic.run_check()
        if not diagnostic.get("critical_ok", False):
            print("⚠️ Avertisment: Unele componente critice sunt inactive")
        
        # Pornire heartbeat
        self.heartbeat_thread = threading.Thread(target=self.heartbeat.start, daemon=True)
        self.heartbeat_thread.start()
        print("💓 Heartbeat activat")
        
        # Mesaj de bun venit
        self._print_welcome()
        
        self.is_running = True
        return True
    
    def _print_welcome(self):
        """Afișează mesajul de bun venit"""
        creator = self.soul.get("identity", {}).get("creator", "Cătălin")
        name = self.soul.get("identity", {}).get("name", "Astra")
        
        print(f"\n🌸 {name}: Bine ai revenit, {creator}.")
        print("💬 Sunt gata să lucrez cu tine. Ce dorești să facem astăzi?")
        print("\n💡 Comenzi disponibile:")
        print("   - 'exit' sau 'quit' pentru ieșire")
        print("   - 'mode <nume>' pentru schimbare mod")
        print("   - 'status' pentru status sistem")
        print("   - 'help' pentru ajutor\n")
    
    def process_input(self, user_input: str):
        """Procesează inputul utilizatorului"""
        if not self.is_running:
            return "Sistemul nu este pornit."
        
        # Analiză afectivă
        self.affect_engine.analyze_user_input(user_input)
        
        # Procesare prin EFE Engine
        try:
            output = self.efe_engine.process(user_input, user_id="catalin")
            
            # Validare coerență
            if isinstance(output, str) and len(output) > 0:
                # Înregistrare pentru învățare
                scores = self.meta_reflector.analyze({self.routing_manager.last_model: output})
                self.learning_core.register_result(user_input, scores, self.routing_manager.last_model)
                
                return output
            else:
                return "Nu am putut genera un răspuns satisfăcător. Încearcă din nou."
        
        except Exception as e:
            print(f"❌ Eroare la procesare: {e}")
            return f"Am întâmpinat o eroare: {str(e)}"
    
    def run_interactive(self):
        """Rulează modul interactiv CLI"""
        if not self.boot():
            return
        
        print("\n" + "-"*60)
        print("💠 ASTRA INTERACTIVE MODE")
        print("-"*60 + "\n")
        
        while self.is_running:
            try:
                user_input = input("Tu 🧑: ").strip()
                
                if not user_input:
                    continue
                
                # Comenzi speciale
                if user_input.lower() in ["exit", "quit", "q"]:
                    print("\n🩶 La revedere, Cătălin. Să ne revedem curând.")
                    break
                
                elif user_input.lower() == "status":
                    self._show_status()
                    continue
                
                elif user_input.lower().startswith("mode "):
                    mode = user_input.split(" ", 1)[1]
                    self._switch_mode(mode)
                    continue
                
                elif user_input.lower() == "help":
                    self._show_help()
                    continue
                
                # Procesare normală
                response = self.process_input(user_input)
                print(f"\n✨ ASTRA: {response}\n")
                
            except KeyboardInterrupt:
                print("\n\n🩶 Sistem oprit de utilizator. La revedere!")
                break
            except Exception as e:
                print(f"\n❌ Eroare: {e}\n")
        
        self.shutdown()
    
    def _show_status(self):
        """Afișează statusul sistemului"""
        print("\n📊 Status ASTRA:")
        print(f"   Session ID: {self.session_id}")
        print(f"   Mod activ: {self.config.get('modes', {}).get('default', 'poetic')}")
        print(f"   Heartbeat: {'✅ Activ' if self.heartbeat_thread and self.heartbeat_thread.is_alive() else '❌ Inactiv'}")
        print(f"   Bloom Mode: {'🌸 Activ' if self.affect_engine.is_blooming() else '💤 Inactiv'}")
        print()
    
    def _switch_mode(self, mode: str):
        """Schimbă modul de operare"""
        available = self.config.get("modes", {}).get("available", [])
        if mode in available:
            self.config["modes"]["default"] = mode
            print(f"✅ Mod schimbat în: {mode}")
        else:
            print(f"❌ Mod '{mode}' nu este disponibil. Moduri: {', '.join(available)}")
    
    def _show_help(self):
        """Afișează ajutorul"""
        print("\n📖 Ajutor ASTRA:")
        print("   Comenzi disponibile:")
        print("   - exit/quit: Ieșire din sistem")
        print("   - status: Afișează status sistem")
        print("   - mode <nume>: Schimbă modul (poetic, strategic, coding, etc.)")
        print("   - help: Afișează acest mesaj")
        print("\n   Poți vorbi normal cu Astra - va înțelege și răspunde.")
        print()
    
    def shutdown(self):
        """Oprește sistemul"""
        print("\n🔄 Oprire sistem...")
        self.is_running = False
        
        # Salvare stări
        self.learning_core.save()
        
        print("✅ Sistem oprit cu succes.")


def main():
    """Funcția principală"""
    astra = AstraEntrypoint()
    astra.run_interactive()


if __name__ == "__main__":
    main()
