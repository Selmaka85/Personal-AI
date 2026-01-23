# run_astra_nexus_unificat.py – Activator complet pentru ASTRA NEXUS (forma finală)

from entrypoint.astra_entrypoint import interpret_prompt
from meta_core.meta_efe import MetaEFE
from entrypoint.routing_manager import RoutingManager
from entrypoint.loop_controller import LoopController
from astrax2_llm_engine import Astrax2Engine
from astrax2_learning_core import Astrax2Learning

# 🔁 Instanțe centrale
meta_efe = MetaEFE()
routing = RoutingManager()
loop = LoopController()
learning = Astrax2Learning()

# 🧬 Instanța duală AstraX2
astra_x2 = Astrax2Engine()

print("\n🧠 ASTRA NEXUS BOOTED • Forma Finală Activă")
print("🔒 Protecție activă • Meta-EFE supraveghează toate răspunsurile")

# 🎤 Interacțiune simplă prin CLI (poate fi legată de web / voice UI)
while True:
    user_input = input("\nTu 🧑: ")

    if user_input.lower() in ["exit", "quit"]:
        print("\n🩶 Sistem închis. La revedere, Cătălin.")
        break

    # 🎯 1. Interpretare prompt + identificare intenție
    interpreted = interpret_prompt(user_input)
    pilon_target = routing.decide_pilon(interpreted)

    print(f"\n🔄 Pilon activat: {pilon_target.upper()}")

    # 🔁 2. Execută taskul în pilon sau cu AstraX2 dacă fallback/soulcore
    if pilon_target == "soulcore":
        result = astra_x2.execute_task(user_input)
        output = result['best_response']
        learning.register_result(user_input, result['scores'], result['best_model'])
    else:
        output = loop.dispatch_to_pilon(pilon_target, interpreted)

    # ✅ 3. Evaluare finală Meta-EFE
    score = meta_efe.evaluate_output(output)

    if score >= 0.85:
        print(f"\n✨ ASTRA NEXUS: {output}")
    else:
        print("\n🔁 Răspunsul nu a fost satisfăcător. Se activează fallback...")
        new_output = loop.retry_or_reroute(user_input)
        print(f"\n✨ [Refăcut] ASTRA NEXUS: {new_output}")
