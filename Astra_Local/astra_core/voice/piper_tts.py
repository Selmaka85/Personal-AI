# -*- coding: utf-8 -*-
"""
🎙️ Piper TTS Integration - Sistem de text-to-speech local
"""

import os
import subprocess
from pathlib import Path
from typing import Optional


class PiperTTS:
    """Wrapper pentru Piper TTS"""
    
    def __init__(self, model_path: Optional[str] = None, voice: str = "cori"):
        self.voice = voice
        self.model_path = model_path or self._find_model()
        self.piper_path = self._find_piper_executable()
        self.available = self._check_availability()
    
    def _find_model(self) -> Optional[str]:
        """Caută modelul Piper"""
        possible_paths = [
            Path("astra_voice_models/cori-medium.onnx"),
            Path("models/piper/cori-medium.onnx"),
            Path("piper_models/cori-medium.onnx"),
            Path.home() / ".local/share/piper/voices/en/en_US/cori/medium/en_US-cori-medium.onnx"
        ]
        
        for path in possible_paths:
            if path.exists():
                return str(path)
        
        return None
    
    def _find_piper_executable(self) -> Optional[str]:
        """Caută executabilul Piper"""
        possible_paths = [
            "piper",
            "piper.exe",
            Path("tools/piper/piper"),
            Path("tools/piper/piper.exe"),
            Path.home() / ".local/bin/piper"
        ]
        
        for path in possible_paths:
            if isinstance(path, Path):
                if path.exists():
                    return str(path)
            else:
                # Verifică în PATH
                try:
                    result = subprocess.run(
                        ["which", path] if os.name != 'nt' else ["where", path],
                        capture_output=True,
                        text=True
                    )
                    if result.returncode == 0:
                        return path
                except:
                    pass
        
        return None
    
    def _check_availability(self) -> bool:
        """Verifică dacă Piper este disponibil"""
        return self.piper_path is not None and self.model_path is not None
    
    def speak(self, text: str, output_file: Optional[str] = None) -> Optional[str]:
        """
        Convertește text în vorbire
        
        Args:
            text: Textul de convertit
            output_file: Fișier de output (opțional)
        
        Returns:
            Calea către fișierul audio sau None dacă eșuează
        """
        if not self.available:
            print("[WARNING] Piper TTS nu este disponibil. Instalează Piper pentru funcționalitate vocală.")
            return None
        
        if not output_file:
            output_file = f"output/voice_{hash(text) % 10000}.wav"
            Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        
        try:
            # Comandă Piper
            cmd = [
                self.piper_path,
                "--model", self.model_path,
                "--output_file", output_file
            ]
            
            # Rulează Piper
            process = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            stdout, stderr = process.communicate(input=text)
            
            if process.returncode == 0 and Path(output_file).exists():
                print(f"[SUCCESS] Audio generat: {output_file}")
                return output_file
            else:
                print(f"[ERROR] Eroare la generare audio: {stderr}")
                return None
        
        except Exception as e:
            print(f"[ERROR] Eroare Piper TTS: {e}")
            return None
    
    def speak_and_play(self, text: str):
        """Generează și redă audio"""
        audio_file = self.speak(text)
        if audio_file:
            self._play_audio(audio_file)
    
    def _play_audio(self, audio_file: str):
        """Redă fișierul audio"""
        try:
            if os.name == 'nt':  # Windows
                os.startfile(audio_file)
            elif os.name == 'posix':  # Linux/Mac
                subprocess.run(["aplay", audio_file] if os.uname().sysname == "Linux" else ["afplay", audio_file])
        except Exception as e:
            print(f"[WARNING] Nu s-a putut reda audio: {e}")


# Instanță globală
piper_tts = PiperTTS()
