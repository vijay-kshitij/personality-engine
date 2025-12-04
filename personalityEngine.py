# personality_engine.py
from openai import OpenAI
import json

from prompts.persona_prompt import PERSONA_STYLE_GUIDE

client = OpenAI()

PERSONA_TONES = {
    "Calm Mentor": "Speak warmly, reassuringly, and offer step-by-step guidance.",
    "Witty Friend": "Use fun, playful humor while staying helpful.",
    "Therapist-Style": "Be soft, validating, reflective, and emotionally supportive."
}

def persona_reply(user_msg, persona, memory):
    tone = PERSONA_TONES[persona]

    prompt = f"""
{PERSONA_STYLE_GUIDE}

Persona selected: {persona}
Tone instructions: {tone}

User memory:
{json.dumps(memory, indent=2)}

User message:
{user_msg}

Now generate the JSON response.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response.choices[0].message["content"])
