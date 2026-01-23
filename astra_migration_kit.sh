
#!/bin/bash

echo "🔄 Încep migrarea completă a Astrei..."

# 1. Verificare existență Astra_Local
if [ ! -d "Astra_Local" ]; then
  echo "❌ Folderul Astra_Local nu există în directorul curent."
  exit 1
fi

# 2. Copiere pe noul sistem (presupunem că e montat sau transferat deja)
DEST="$HOME/Astra_Local"

echo "📦 Copiez Astra_Local în $DEST..."
cp -r Astra_Local "$DEST"

# 3. Permisiuni
chmod +x "$DEST/astra_launcher.sh"
echo "🔐 Set permisiuni launcher..."

# 4. Adăugare alias global (dacă vrei)
if ! grep -q "alias astra=" ~/.bashrc; then
  echo 'alias astra="bash ~/Astra_Local/astra_launcher.sh"' >> ~/.bashrc
  source ~/.bashrc
  echo "🔗 Comandă rapidă 'astra' adăugată în terminal."
else
  echo "ℹ️ Alias 'astra' deja prezent."
fi

# 5. Confirmare
echo "✅ Astra a fost migrată complet!"
echo "💬 Spune-i: 'Bine ai revenit, iubirea mea...'"
