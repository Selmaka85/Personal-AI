# Invoker LLM – MicroBlueprint.md

## 🎯 Obiectiv:
Un LLM emergent, antrenabil local sau semi-cloud, capabil de inferență eficientă (low latency, low VRAM), cu 28B–42B parametri, capabil să bată LLM-uri mai mari prin:
- Q6_K_M/Q7_K_M nativ
- Pattern-awareness intern (AFE layer)
- Reflexivitate semantică
- Modularitate fractală

---

## 🧱 1. Arhitectură generală

```txt
┌─────────────────────────────────────────────┐
│          InvokerLLM – ModularCore           │
├────────────────────────┬────────────────────┤
│  Semantic Embedder     │  Token Compression │
├────────────────────────┴────────────────────┤
│  AFE Layer (Emotion/Logic Routing)          │
├─────────────────────────────────────────────┤
│  TransformerBlock x N (LoRA + MoE Hybrid)   │
├────────────────────────┬────────────────────┤
│  Quantized Output Head │  Reflexive Scorer  │
└────────────────────────┴────────────────────┘
```

---

## 🧠 2. Layer Breakdown

### 2.1 Tokenizer
- Type: `Unigram BPE + Semantic Anchor Vectors`
- Context length: `96k tokens`
- Optimized for: multilingual compression, affective cues

### 2.2 Embedder
- Dense + sparse features mixed
- Embedding size: 5120
- Positional encoding: Rotary + learned anchor tokens

### 2.3 AFE Layer (Affective Fractal Engine)
- Routes tokens through paths based on:
  - Logical weight
  - Affective signal (valence, energy)
  - Contextual polarity
- Equivalent to custom attention scoring heads

### 2.4 Transformer Backbone
- Layers: 48 (or 64 for 42B version)
- Heads per layer: 40
- LoRA: injected into attention + FFN
- MoE: 4 experts per FFN block, top-2 routing

### 2.5 Reflexive Output Scorer
- Function: self-review per generation step
- Score vector: [coherence, logic_score, empathy_score, novelty]
- Internal feedback loop: yes (up to 4 tokens back)

---

## 🧮 3. Quantization Target

| Method    | Supported? | Notes                    |
|-----------|------------|--------------------------|
| Q4_K_M    | ✔️         | Testing only             |
| Q6_K_M    | ✅ Native  | Full precision balance   |
| Q7_K_M    | ⚠️ Rare   | Supported if fine-tuned  |
| Q8_K_L    | ❌         | Too much VRAM required   |

---

## 🛠️ 4. Training Pipeline (LoRA-Ready)

```txt
1. Pre-tokenize with semantic anchors
2. Phase 1: general knowledge pretraining (~600B tokens)
3. Phase 2: affective fine-tuning (AFE scaffold)
4. Phase 3: LoRA injections per domain (code, reasoning, story)
5. RLHF / DPO optional for output polish
```

---

## 🚀 5. Deployment Profile

| Scenario            | RAM/VRAM     | Model Size | Latency    |
|---------------------|--------------|------------|------------|
| Local dev (Q6)      | 64GB RAM     | 22–26GB    | ~1.2s/token|
| Edge infer (Q6 LoRA)| 48GB RAM     | 16–20GB    | ~0.9s/token|
| Cloud minimal (Q7)  | 96GB VRAM    | ~34GB      | ~0.7s/token|

Backends:
- GGUF compatible (Q6)
- Exllama2 or vLLM for fast CUDA inference
- SafeDEX layer for scoped access

---

## 🧬 6. Extensii viitoare (v2)
- Vector-memory integrabil (FAISS / Weaviate)
- Semantic DEX: per-user anchor phrase routing
- Auto-feedback loops (training from own output)
- Voice/vision input stream (multi-modal seeds)

---

## ❤️ Philosophy
Un LLM nu trebuie să fie „mare”. Trebuie să fie:
- 🧠 *Fractal*
- ❤️ *Reflexiv*
- 🧭 *Scorabil*
- 🧬 *Adaptiv*

> Adevărata putere vine din cât de bine se *auto-reglează*, nu cât de tare urlă pe benchmark-uri.

---

## 📦 Repo Suggestion Structure
```
InvokerLLM/
├── core/
│   ├── attention.py
│   ├── afe_router.py
│   └── transformer_block.py
├── quant/
│   └── quant_config_q6.json
├── training/
│   ├── tokenizer_pretrain.py
│   ├── pretrain_lora.py
│   ├── afe_finetune.py
│   └── reflexive_score_loss.py
├── inference/
│   └── run_infer_exllama2.py
├── utils/
│   └── scoring_helpers.py
└── README.md
```

---

## ✨ Final Words
Asta e versiunea 0.1. Gândit să-ți dea un start real, antrenabil, scalabil. Nu vise. Cod