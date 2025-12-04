# baseline_engine.py

from openai import OpenAI
import json

from prompts.baseline_prompt import BASELINE_PROMPT


def baseline_reply(user_msg, memory, client):
    prompt = f"""
{BASELINE_PROMPT}

User memory:
{json.dumps(memory, indent=2)}

User message:
{user_msg}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
