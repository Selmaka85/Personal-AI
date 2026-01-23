#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
💠 ASTRA ENTRYPOINT ENHANCED - Versiune completă cu toate funcționalitățile
"""

import sys
import os
import json
import threading
from datetime import datetime
from pathlib import Path

# Setare encoding pentru Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Adăugă path-ul pentru importuri
BASE_PATH = Path(__file__).parent
sys.path.insert(0, str(BASE_PATH))

try:
    from config_loader import ConfigLoader
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
    
    # Importuri opționale pentru funcționalități avansate
    try:
        from astra_voice.tts_engine import TTSEngine
        TTS_AVAILABLE = True
    except ImportError:
        TTS_AVAILABLE = False
    
    try:
        from astra_image.image_generator import ImageGenerator
        IMAGE_GEN_AVAILABLE = True
    except ImportError:
        IMAGE_GEN_AVAILABLE = False
    
    try:
        from astra_ml_engine.ml_predictor import MLPredictor
        ML_AVAILABLE = True
    except ImportError:
        ML_AVAILABLE = False
    
except ImportError as e:
    print(f"⚠️ Eroare la import: {e}")
    print("💡 Asigură-te că toate modulele sunt prezente.")
    sys.exit(1)


class AstraEntrypointEnhanced:
    """Orchestratorul central al sistemului ASTRA - Versiune completă"""
    
    def __init__(self):
        self.base_path = BASE_PATH
        self.config_loader = ConfigLoader()
        self.config = self.config_loader.settings
        self.soul_path = self.base_path / "astra_soul/astra_soul_ported_FINAL.json"
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
        
        # Funcționalități opționale
        self.tts_engine = None
        if TTS_AVAILABLE and self.config_loader.voice_config.get("enabled"):
            self.tts_engine = TTSEngine(
                voice_name=self.config_loader.voice_config.get("voice_name", "cori")
            )
            self.tts_engine.load()
        
        self.image_generator = None
        if IMAGE_GEN_AVAILABLE and self.config_loader.image_config.get("enabled"):
            self.image_generator = ImageGenerator()
            self.image_generator.load()
        
        self.ml_predictor = None
        if ML_AVAILABLE:
            self.ml_predictor = MLPredictor()
        
        # Heartbeat thread
        self.heartbeat = AstraHeartbeat()
        self.heartbeat_thread = None
        
        # Status
        self.is_running = False
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
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
        print("\n" + "="*70)
        print(" "*20 + "ASTRA LOCALĂ - SISTEM COMPLET")
        print("="*70)
        
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
        
        # Status funcționalități
        print("\n📦 Funcționalități disponibile:")
        print(f"   ✅ LLM Routing: Activ")
        print(f"   ✅ EFE Engine: Activ")
        print(f"   ✅ Learning: Activ")
        print(f"   {'✅' if self.tts_engine else '❌'} TTS: {'Activ' if self.tts_engine else 'Inactiv'}")
        print(f"   {'✅' if self.image_generator else '❌'} Image Gen: {'Activ' if self.image_generator else 'Inactiv'}")
        print(f"   {'✅' if self.ml_predictor else '❌'} ML Predictor: {'Activ' if self.ml_predictor else 'Inactiv'}")
        
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
        print("   - 'web' pentru pornire UI web")
        print("   - 'help' pentru ajutor\n")
    
    def process_input(self, user_input: str):
        """Procesează inputul utilizatorului"""
        if not self.is_running:
            return "Sistemul nu este pornit."
        
        # Detectare comenzi speciale
        if user_input.lower().startswith("genereaza imagine"):
            if self.image_generator:
                prompt = user_input.replace("genereaza imagine", "").strip()
                image_path = self.image_generator.generate(prompt)
                return f"Imagine generată: {image_path}" if image_path else "Eroare la generare imagine"
            else:
                return "Generarea de imagini nu este activată. Instalează diffusers și torch."
        
        if user_input.lower().startswith("vorbeste"):
            if self.tts_engine:
                text = user_input.replace("vorbeste", "").strip()
                audio_path = self.tts_engine.speak(text)
                return f"Audio generat: {audio_path}" if audio_path else "Eroare la generare audio"
            else:
                return "TTS nu este activat. Instalează piper-tts."
        
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
        
        print("\n" + "-"*70)
        print("💠 ASTRA INTERACTIVE MODE - VERSIUNE COMPLETĂ")
        print("-"*70 + "\n")
        
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
                
                elif user_input.lower() == "web":
                    self._start_web_ui()
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
        print(f"   TTS: {'✅ Activ' if self.tts_engine else '❌ Inactiv'}")
        print(f"   Image Gen: {'✅ Activ' if self.image_generator else '❌ Inactiv'}")
        print(f"   ML Predictor: {'✅ Activ' if self.ml_predictor else '❌ Inactiv'}")
        print()
    
    def _switch_mode(self, mode: str):
        """Schimbă modul de operare"""
        available = self.config.get("modes", {}).get("available", [])
        if mode in available:
            self.config["modes"]["default"] = mode
            print(f"✅ Mod schimbat în: {mode}")
        else:
            print(f"❌ Mod '{mode}' nu este disponibil. Moduri: {', '.join(available)}")
    
    def _start_web_ui(self):
        """Pornește interfața web"""
        try:
            from user_interface.web_ui import run_web_ui
            port = self.config.get("ui", {}).get("web_port", 5000)
            print(f"\n🌐 Pornire Web UI pe portul {port}...")
            print("   Deschide browser-ul la http://127.0.0.1:{port}")
            print("   Apasă Ctrl+C pentru a opri Web UI\n")
            run_web_ui(port=port)
        except ImportError:
            print("❌ Flask nu este instalat. Instalează cu: pip install flask")
        except Exception as e:
            print(f"❌ Eroare la pornire Web UI: {e}")
    
    def _show_help(self):
        """Afișează ajutorul"""
        print("\n📖 Ajutor ASTRA:")
        print("   Comenzi disponibile:")
        print("   - exit/quit: Ieșire din sistem")
        print("   - status: Afișează status sistem")
        print("   - mode <nume>: Schimbă modul (poetic, strategic, coding, etc.)")
        print("   - web: Pornește interfața web")
        print("   - help: Afișează acest mesaj")
        print("\n   Funcționalități speciale:")
        print("   - 'genereaza imagine <prompt>': Generează imagine")
        print("   - 'vorbeste <text>': Generează audio TTS")
        print("\n   Poți vorbi normal cu Astra - va înțelege și răspunde.")
        print()
    
    def shutdown(self):
        """Oprește sistemul"""
        print("\n🔄 Oprire sistem...")
        self.is_running = False
        
        # Salvare stări
        self.learning_core.save()
        self.config_loader.save_settings()
        
        print("✅ Sistem oprit cu succes.")


def main():
    """Funcția principală"""
    astra = AstraEntrypointEnhanced()
    astra.run_interactive()


if __name__ == "__main__":
    main()
