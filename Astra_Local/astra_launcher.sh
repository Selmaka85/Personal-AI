#!/bin/bash
# ASTRA Local Launcher pentru Linux/MacOS

echo ""
echo "========================================"
echo "   ASTRA LOCALA - SYSTEM LAUNCHER"
echo "========================================"
echo ""

# Verificare Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 nu este instalat!"
    echo "Instaleaza Python 3.8+ de la https://www.python.org/"
    exit 1
fi

# Navigare la directorul ASTRA
cd "$(dirname "$0")"

# Verificare fișiere esențiale
if [ ! -f "astra_entrypoint.py" ]; then
    echo "[ERROR] astra_entrypoint.py nu a fost gasit!"
    exit 1
fi

# Pornire ASTRA
echo "[INFO] Pornire ASTRA..."
echo ""
python3 astra_entrypoint.py
