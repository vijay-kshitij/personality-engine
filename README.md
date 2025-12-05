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

👉 **URL:** *[Live App](https://personality-engine-assign.streamlit.app/)*

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
<img width="762" height="403" alt="Screenshot 2025-12-05 at 12 11 15 PM" src="https://github.com/user-attachments/assets/95dca2e1-f15b-4e5f-bb53-583c646862f3" />

---

Calm Mentor
<img width="788" height="607" alt="Screenshot 2025-12-05 at 12 04 06 PM" src="https://github.com/user-attachments/assets/c917e235-771e-4f93-8129-7ad7054538fa" />

---

Witty Friend
<img width="774" height="511" alt="Screenshot 2025-12-05 at 12 10 01 PM" src="https://github.com/user-attachments/assets/ead56c27-ff5e-4cde-b304-6c43eb8811a3" />

---

Therapist
<img width="731" height="503" alt="Screenshot 2025-12-05 at 12 12 12 PM" src="https://github.com/user-attachments/assets/d9b52115-b0db-4fac-a34b-8a7bb37b5e40" />

---

Professional Coach
<img width="739" height="509" alt="Screenshot 2025-12-05 at 12 12 55 PM" src="https://github.com/user-attachments/assets/684d50c0-4e4c-43f7-a40b-f89e38c9391d" />

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


