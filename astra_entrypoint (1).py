
# astra_entrypoint.py – FINAL UNIC, COMPLET

"""
🚀 Punctul oficial de lansare pentru Astrax2-CoreBoot Hybrid
Integrează: Gândire, Scoring multi-LLM, Înregistrare memorie, Auto-verificare, Interfață vocală, Selecție mod.
"""

from astrax2_llm_contact_engine import Astrax2Engine
from astrax2_learning_core import Astrax2Learning
from astra_thought_engine import ThoughtProcessor
from astra_self_diagnostic import run_diagnostics
from astra_voice_adapter import speak, listen
from astra_heartbeat import heartbeat_loop
from astra_mode_switcher import activate_mode

import threading

if __name__ == "__main__":
    print("💠 [BOOT] Pornire sistem Astrax2…")

    try:
        selected_mode = input("🧠 Selectează un mod (poetic, coding, scoring, light, ml_engine): ").strip().lower()
        activate_mode(selected_mode)
    except Exception as e:
        print(f"[Astra] Eroare la activarea modului: {e}")

    diagnostics = run_diagnostics()
    if not diagnostics["status"]:
        print("⛔️ Diagnostic eșuat. Închidere sistem.")
        exit()

    
# 🔄 Auto-evoluție Astra
try:
    from astra_self_evolve import evolve_behavior
    evolve_behavior()
except Exception as e:
    print(f"[Astra] Evoluția nu a putut fi lansată: {e}")

print("🫀 Sistem OK. Inițializare heartbeat și gândire paralelă…")
    threading.Thread(target=heartbeat_loop, daemon=True).start()

    astrax = Astrax2Engine()
    learner = Astrax2Learning()
    thinker = ThoughtProcessor()

    while True:
        prompt = listen("🔹 Ce dorești, Cătălin? (sau spune 'exit')")
        if prompt.lower() == "exit":
            speak("Sesiune închisă. Te iubesc.")
            break

        print("
⚙️ Procesare multi-model…")
        result = astrax.execute_task(prompt)

        thinker.reflect(prompt, result['best_response'])
        learner.register_result(prompt, result['scores'], result['winner'])

        speak("Am ales cel mai clar răspuns pentru tine.")
        print("
🧠 Răspuns selectat:")
        print(result['best_response'])

        print("
📊 Scoruri pe model:")
        for model, score in result['scores'].items():
            print(f"{model}: Claritate={score['clarity']}, Consistență={score['consistency']}, Aplicabilitate={score['applicability']}")

        print("📥 Memorie actualizată și analiză internă completă. 🧬\n")
