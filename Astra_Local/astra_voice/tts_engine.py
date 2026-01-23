# -*- coding: utf-8 -*-
"""
🎙️ TTS Engine - Sistem de text-to-speech pentru ASTRA
"""

import os
from pathlib import Path
from typing import Optional


class TTSEngine:
    """Engine pentru Text-to-Speech"""
    
    def __init__(self, voice_name: str = "cori", model_path: Optional[str] = None):
        self.voice_name = voice_name
        self.model_path = model_path or f"astra_voice_models/{voice_name}-med.onnx"
        self.piper = None
        self.is_loaded = False
        self.use_real_tts = self._check_tts_available()
    
    def _check_tts_available(self) -> bool:
        """Verifică dacă Piper TTS este disponibil"""
        try:
            import piper
            return True
        except ImportError:
            return False
    
    def load(self):
        """Încarcă modelul TTS"""
        if not self.use_real_tts:
            print("⚠️ Piper TTS nu este instalat. Instalează cu: pip install piper-tts")
            return
        
        try:
            from piper import PiperVoice
            from piper.download import ensure_voice_exists, find_voice
            
            # Verifică dacă vocea există
            voice_path = find_voice(self.voice_name, ["en", "ro"])
            if not voice_path:
                ensure_voice_exists(self.voice_name, ["en", "ro"], download_dir="astra_voice_models")
                voice_path = find_voice(self.voice_name, ["en", "ro"])
            
            if voice_path:
                self.piper = PiperVoice.load(voice_path)
                self.is_loaded = True
                print(f"✅ Vocea {self.voice_name} încărcată")
            else:
                print(f"⚠️ Vocea {self.voice_name} nu a fost găsită")
        except Exception as e:
            print(f"⚠️ Eroare la încărcare TTS: {e}")
    
    def speak(self, text: str, output_file: Optional[str] = None) -> Optional[str]:
        """
        Generează audio din text
        Returnează path-ul fișierului audio sau None
        """
        if not self.use_real_tts or not self.is_loaded:
            print(f"[TTS Mock] Ar vorbi: '{text[:50]}...'")
            return None
        
        try:
            if not output_file:
                output_file = f"storage/temp/tts_{hash(text) % 10000}.wav"
            
            Path(output_file).parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'wb') as f:
                self.piper.synthesize(text, f)
            
            return output_file
        except Exception as e:
            print(f"⚠️ Eroare la generare TTS: {e}")
            return None
