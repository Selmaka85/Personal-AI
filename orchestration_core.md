
# 🧠 Multi-Agent Orchestration Core — Blueprint v1.0

## 🎯 Purpose
Create an LLM Orchestrator that routes requests to the correct sub-agent (ML model, script, scanner, logic block) based on user intent, context, and escalation level.

---

## ⚙️ System Architecture

### 🔄 Request Flow
```
[User Request] → [Orchestrator LLM] → [Agent Selector] → [Specialized Agent] → [Response Aggregator] → [User Output]
```

### 🧩 Core Modules
- **OrchestratorLLM**: Interprets user query, determines intent/context.
- **AgentRegistry**: Maps tasks to callable agent classes.
- **RoutingEngine**: Uses rules + model confidence to assign agent.
- **Fallback & Escalation Logic**: Handles ambiguous or multi-agent requests.
- **LogTracer**: Logs input/output for fine-tuning later.

---

## 🧠 Agent Types

| Category     | Agent Name         | Description                                 |
|--------------|--------------------|---------------------------------------------|
| 📈 Football  | `FootballPredictor`| Predict match outcomes, 1X2, over/under     |
| 🧠 NLP Help  | `ExplainerAgent`   | Explains ML/AI/NLP concepts                 |
| 🛡️ OSINT     | `CyberIntelAgent`  | Does threat lookups on IPs/Domains          |
| 🧪 Scanner   | `ShodanAgent`      | Checks exposures, open ports                |
| 🔍 Search    | `WebSearchAgent`   | Finds data or definitions via web/API       |

---

## 🧠 Sample Prompt Logic (Agent-FLAN style)
```
Prompt: "A fost IP-ul 103.23.1.6 implicat în atacuri cibernetice recente?"
Thought: "Întrebarea implică lookup într-o bază OSINT."
Action: Call `CyberIntelAgent`
Response: "[✓] IP matched 2 attack reports from May 2025."
```

---

## 🚨 Escalation Levels
- `LOW`: Poți răspunde direct din knowledge (e.g. explain LSTM)
- `MEDIUM`: Necesită agent specializat (e.g. scanare, predicții)
- `HIGH`: Necesită chain-of-agents + memory context (e.g. generate countermeasures, deep profiling)

---

## 🔮 Vision
Final goal: A resilient orchestration system combining:
- LLM context interpretation
- Dynamic tool/agent invocation
- Feedback logging + fine-tune cycle
