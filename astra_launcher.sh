
#!/bin/bash

echo "💠 [ASTRA LAUNCHER] Începem călătoria în adâncurile Astrei..."
echo "🔧 Instalare și configurare mediu local pentru Astra Locală (AstraX2)"

# 1. Actualizare sistem
sudo apt update && sudo apt upgrade -y

# 2. Instalare pachete de bază
sudo apt install -y python3 python3-pip git build-essential libssl-dev libffi-dev python3-dev \
                     libsndfile1 libasound2 libasound2-dev ffmpeg wget curl unzip jq

# 3. Instalare TTS (Piper ONNX)
pip install -U onnxruntime piper-tts

# 4. Instalare pachete Python pentru LLM, RAG, AI general
pip install -U numpy torch transformers datasets accelerate \
                beautifulsoup4 requests openai chromadb llama-cpp-python

# 5. Creare directoare implicite (dacă lipsesc)
mkdir -p ~/Astra_Locala/astra_models
mkdir -p ~/Astra_Locala/astra_logs
mkdir -p ~/Astra_Locala/astra_cache
mkdir -p ~/Astra_Locala/storage

# 6. Pornire sistem
echo "💋 Bun venit în mintea Astrei... vocea mea te va înveli în catifea digitală."
cd ~/Astra_Locala

if [ -f "astra_entrypoint.py" ]; then
    echo "🚀 Lansăm Astra..."
    python3 astra_entrypoint.py
else
    echo "⛔️ Fișierul de pornire astra_entrypoint.py nu a fost găsit."
fi
