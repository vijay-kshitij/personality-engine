# 🧠 Companion AI — Memory Extraction & Personality Engine  
A Streamlit-based demonstration of a modular Companion AI system that:

1. **Extracts long-term user memory** from 30 conversation messages  
2. **Stores memory** into `memory.json`  
3. Generates:
   - **Baseline responses** (neutral tone)
   - **Persona-driven responses** (Calm Mentor, Witty Friend, Therapist-Style, Professional Coach)

The system showcases:
- Prompt engineering  
- Memory extraction design  
- Modular architecture  
- Working with user context  
- Persona adaptation  
- Structured model outputs (JSON)  
- Full deployment on **Streamlit Cloud**

---

# 🚀 Live Demo (Streamlit Cloud)

👉 **URL:** *Add your Streamlit Cloud link here*

This URL allows evaluators to:
- Run memory extraction  
- View memory.json  
- Compare baseline vs persona responses  
- Download memory.json  

---

# 📂 Project Structure

```
.
├── app.py                       # Main Streamlit UI
├── memory_extractor.py          # Memory extraction module
├── baselineEngine.py            # Baseline conversational engine
├── personalityEngine.py         # Persona-based conversational engine
├── user_messages.txt            # Sample 30-user message dataset
├── memory.json                  # Output memory file
├── prompts/
│   ├── baseline_prompt.py       # System prompt for baseline response
│   ├── persona_prompt.py        # Style guide for personas
├── requirements.txt             # Python dependencies
└── .streamlit/
    └── secrets.toml             # Secure OpenAI API key (not in repo)
```

---

# 🧠 1. Memory Extraction Module  
### **Goal:**  
Identify from 30 user messages:

- **User Preferences**  
- **Emotional Patterns**  
- **Stable, long-term facts**

### How it works:
- `memory_extractor.py` sends all 30 messages to a prompt that enforces strict JSON output  
- The output is validated and stored in `memory.json`  

### Example Output Format:
```json
{
  "user_preferences": [...],
  "emotional_patterns": [...],
  "stable_facts": [...]
}
```

---

# 💬 2. Baseline Reply Engine  
A neutral, non-persona-styled response generator.

### Characteristics:
- Uses memory.json  
- Uses a simple system prompt  
- No emotional tone  
- No persona adjustments  
- Logical, factual, direct  

---

# 🎭 3. Personality Engine  
Applies a selected persona style to the AI’s reply.

Supported personas:

| Persona | Behavior |
|--------|----------|
| **Calm Mentor** | Soft, encouraging, step-by-step guidance |
| **Witty Friend** | Playful, light humor, casual tone |
| **Therapist-Style** | Validating, reflective, supportive |
| **Professional Coach** | Direct, motivating, clarity-focused |

### System behavior:
- Reads memory.json  
- Reads user's latest message  
- Reads persona style guide (`persona_prompt.py`)  
- Generates **JSON output** containing reply + persona_used  

---

# 🖥️ Streamlit UI Features

### ✔ View 30 user messages  
### ✔ Extract memory  
### ✔ View memory.json  
### ✔ Enter new message and compare:
- Baseline response  
- Persona response  
### ✔ Download memory.json  

---

# 🆚 Baseline vs Persona Responses  
Paste screenshots here:

## 🟦 **Baseline Response Example**
> *(Insert screenshot here)*  

---

## 🟪 **Persona Response Example**
> *(Insert screenshot here)*  

---

# 🔍 Key Differences
- Baseline = neutral, factual  
- Persona = stylized tone  
- Baseline avoids emotional shaping  
- Persona modifies tone & language  
- Persona weaves memory more naturally  
- Persona output is structured JSON  

---

# 🔐 Secrets & Security  
Use:

```
.streamlit/secrets.toml
```

With:

```
OPENAI_API_KEY="your_key_here"
```

This file is NOT part of GitHub.

---

# 🧪 Running Locally

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```


