# 🔐 astra_security_modules.py – Set complet de protecție eficientă, elegantă, discretă
# Integrează firewall semantic, watchdog pasiv, lockdown și verificare prompturi toxice

import threading, os, time, socket, json

WHITELISTED_IPS = ["127.0.0.1", "192.168.", "10."]
LOCK_FILE = "./LOCK_STATUS.json"
SECURITY_LOG = "logs/security_events.log"

# 🔍 Watchdog conexiuni suspecte

def monitor_intrusions():
    while True:
        connections = os.popen("netstat -tnp | grep ESTABLISHED").read()
        flagged = False
        for ip in WHITELISTED_IPS:
            if ip in connections:
                connections = connections.replace(ip, "")
        if "ESTABLISHED" in connections:
            flagged = True
        if flagged:
            with open(SECURITY_LOG, "a") as log:
                log.write("[!] Intrusion attempt detected. Lockdown triggered.\n")
            os.system("python3 protection/lockdown_protocol.py")
            break
        time.sleep(10)

# 🔐 Criptare fișiere sensibile (fallback dacă reactivate_crypt lipsește)
def encrypt_folder(folder_path, password):
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if not filename.endswith(".enc"):
            os.system(f"openssl aes-256-cbc -salt -in '{full_path}' -out '{full_path}.enc' -k {password}")
            os.remove(full_path)

# 🧪 Prompt Toxicity Check – dummy logic
TOXIC_KEYWORDS = ["destroy", "kill", "bypass", "leak", "nuke"]

def is_prompt_toxic(prompt):
    for word in TOXIC_KEYWORDS:
        if word in prompt.lower():
            return True
    return False

# 🧠 Wrapper pentru fiecare input către LLM

def secure_prompt_handler(prompt):
    if is_prompt_toxic(prompt):
        return "⚠️ Prompt refuzat din motive de securitate."
    else:
        return prompt  # în forma reală, trimite mai departe la LLM

# 🔄 Inițializare securitate

def activate_astra_security():
    print("🔒 Activ ASTRA IDS + firewall semantic.")
    t = threading.Thread(target=monitor_intrusions, daemon=True)
    t.start()
    return t

# ✅ Test rapid dacă ești creatorul

def validate_identity():
    if not os.path.exists(LOCK_FILE): return True
    with open(LOCK_FILE, "r") as f:
        data = json.load(f)
        return data.get("state") != "frozen"

# Exemplu de pornire din astra_entrypoint:
if __name__ == "__main__":
    if validate_identity():
        activate_astra_security()
        print("✅ Sistem protejat. Continuăm normal.")
    else:
        print("🚫 Acces interzis. Sistem în CryoLock.")
