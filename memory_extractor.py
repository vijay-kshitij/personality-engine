# memory_extractor.py
from openai import OpenAI
import json

client = OpenAI()

def extract_memory(messages):
    prompt = f"""
Your job:
- Read raw user messages
- Extract ONLY long-term, stable memories
- Identify 3 types of memories:
    1. Preferences
    2. Emotional Patterns
    3. Facts Worth Remembering

Rules:
- Keep only memories that will matter months from now.
- Do NOT store temporary feelings or daily events.
- Do NOT infer or guess beyond what is written.
- Ignore chit-chat, greetings, filler sentences.
- Do not duplicate memories.

Output a STRICT JSON object:
{{
  "preferences": [],
  "emotional_patterns": [],
  "facts": []
}}

Do NOT add anything not directly stated.
Do NOT include explanations.

User messages:
{messages}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    memory = json.loads(response.choices[0].message["content"])
    return memory
