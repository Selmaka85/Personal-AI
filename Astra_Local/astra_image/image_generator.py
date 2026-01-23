# -*- coding: utf-8 -*-
"""
🎨 Image Generator - Sistem de generare imagini pentru ASTRA
"""

import os
from pathlib import Path
from typing import Optional, Dict, Any


class ImageGenerator:
    """Generator de imagini folosind Stable Diffusion"""
    
    def __init__(self, model_name: str = "stable-diffusion-xl"):
        self.model_name = model_name
        self.pipeline = None
        self.is_loaded = False
        self.use_real_generator = self._check_generator_available()
    
    def _check_generator_available(self) -> bool:
        """Verifică dacă generatorul este disponibil"""
        try:
            import torch
            from diffusers import StableDiffusionXLPipeline
            return True
        except ImportError:
            return False
    
    def load(self):
        """Încarcă modelul de generare imagini"""
        if not self.use_real_generator:
            print("⚠️ diffusers nu este instalat. Instalează cu: pip install diffusers transformers accelerate")
            return
        
        try:
            from diffusers import StableDiffusionXLPipeline
            import torch
            
            device = "cuda" if torch.cuda.is_available() else "cpu"
            
            self.pipeline = StableDiffusionXLPipeline.from_pretrained(
                "stabilityai/stable-diffusion-xl-base-1.0",
                torch_dtype=torch.float16 if device == "cuda" else torch.float32,
                use_safetensors=True
            )
            self.pipeline = self.pipeline.to(device)
            self.is_loaded = True
            print(f"✅ Image generator încărcat pe {device}")
        except Exception as e:
            print(f"⚠️ Eroare la încărcare generator: {e}")
    
    def generate(self, prompt: str, negative_prompt: str = "", 
                 width: int = 1024, height: int = 1024,
                 num_inference_steps: int = 50,
                 output_path: Optional[str] = None) -> Optional[str]:
        """
        Generează imagine din prompt
        Returnează path-ul fișierului imagine sau None
        """
        if not self.use_real_generator or not self.is_loaded:
            print(f"[Image Mock] Ar genera imagine pentru: '{prompt[:50]}...'")
            return None
        
        try:
            if not output_path:
                output_path = f"storage/temp/image_{hash(prompt) % 10000}.png"
            
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            
            image = self.pipeline(
                prompt=prompt,
                negative_prompt=negative_prompt,
                width=width,
                height=height,
                num_inference_steps=num_inference_steps
            ).images[0]
            
            image.save(output_path)
            print(f"✅ Imagine generată: {output_path}")
            return output_path
        except Exception as e:
            print(f"⚠️ Eroare la generare imagine: {e}")
            return None
