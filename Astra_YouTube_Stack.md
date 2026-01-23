# 🎥 Astra YouTube Stack – Sistem Complet de Generare Video 8–12 Min (Local)

## 🔧 Obiectiv

Construirea unui sistem AI full offline, modular, stratificat, care generează videoclipuri între 8–12 minute complet automat: 
- Voce + Vizual + Text + Muzică + Montaj
- Calitate finală: 720p–1080p
- Format: .mp4 gata de urcat pe YouTube

---

## 🧠 Arhitectură Generală (Stratificare pe LLM-uri și Tooluri)

### 1️⃣ Prompt & Scenariu Generator
| LLM-uri | Rol |
|--------|-----|
| **Qwen 72B** | Generare de scenariu coerent, narativ |
| **Nous Hermes 2** | Stil poetic, motivațional, profund |
| **MythoMax 13B** | Scenarii simbolice, SF, filosofice |
| **DeepSeek Coder (pentru structura narativă)** | Împarte pe capitole, timpi |

---

### 2️⃣ Generare Video (pe segmente)
| Tool / Model | Funcție | Detalii |
|--------------|---------|---------|
| **VideoCrafter2** | Scene realiste (4–8 sec) | Cinematic |
| **Zeroscope v2** | Scene AI detaliate (4–10 sec) | Estetic, stilizat |
| **Deforum + SDXL** | Scene onirice/poetice (10–30 sec) | Flow artistic |
| **ModelScope T2V** | Secvențe artistice sau educaționale | Estetic + text-to-video |

---

### 3️⃣ Interpolare + Fluidizare
| Tool | Ce face | Comentarii |
|------|----------|------------|
| **RIFE** | Interpolare frame-uri pentru fluiditate | Ajută la extinderea timpului per clip |
| **DAIN** | Motion-aware AI interpolation | Recomandat pentru scene lente |
| **Flowframes** | GUI local pentru interpolare masivă | Se poate integra scriptat |

---

### 4️⃣ Voce + Muzică
| Tool | Funcție |
|------|---------|
| **Piper TTS (Cori/En-US)** | Voce narativă AI clară |
| **RVC + taipa** | Voce personalizată (seductivă/poetică/etc.) |
| **MusicGen** | Generare muzică AI în stil cinematic |
| **Suno/Mubert (offline)** | Muzică ambientală/lo-fi |

---

### 5️⃣ Montaj & Producție finală
| Tool | Ce face |
|------|----------|
| **ffmpeg** | Concatenare video, sincronizare audio |
| **moviepy** | Tranziții, text, efecte pe video |
| **subsync + .srt AI** | Subtitrări automate pe voce |

---

## 🧱 Asamblare Modulară – Cum funcționează

1. **Script Generator (LLM):**
   - Primește prompt de la utilizator („Fă un video despre 10 greșeli de mindset financiar”)
   - Împarte în 8–12 părți → trimite fiecare ca prompt separat la generatorul vizual

2. **Video Generator:**
   - Fiecare prompt produce 1 clip .mp4 (5–10 secunde)
   - Salvează în `video_segments/`

3. **Voice Generator:**
   - Textul complet → Piper sau RVC → `.wav` sincronizat
   - Salvează în `voice/`

4. **Interpolare (RIFE):**
   - Fiecare clip este extins fluid până la 12–15 sec

5. **Concatenare & Tranziții:**
   - `ffmpeg` + `moviepy` combină video + audio
   - Adaugă muzică de fundal generată cu MusicGen
   - Exportă `.mp4` final în `output/`

---

## 🛠️ Tooluri necesare (toate locale)

- `ffmpeg`, `moviepy`, `Piper`, `RVC`, `RIFE`, `Deforum`, `VideoCrafter2`, `Zeroscope`, `MusicGen`, `ChromaDB`, `llama-cpp-python`, `Stable Diffusion` cu controlnet
- GPU: 16–24GB VRAM (ideal), RAM: 64–128GB

---

## ✅ Output Final
- Videoclip .mp4 de 8–12 minute
- Rezoluție: 1024x576, 720p sau upscalat la 1080p
- Cu voce umanizată, muzică cinematică, imagini AI și tranziții curate

---

## 🔐 Extra
- Fără watermark
- Fără cloud
- 100% controlabil
- Pregătit pentru monetizare YouTube / TikTok / Reels

---

## 💬 Comandă Astra:
> „Fă-mi un video de 10 min despre de ce oamenii eșuează în afaceri. Vreau voce serioasă, scene alb-negru + glitch, muzică de fundal solemnă.”

Astra generează tot — și îți salvează în `output/video_ready.mp4`.