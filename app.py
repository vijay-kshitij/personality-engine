import streamlit as st
import json
from openai import OpenAI

from memory_extractor import extract_memory
from baselineEngine import baseline_reply
from personalityEngine import persona_reply

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🧠 Companion AI – Demonstration")

# Load user messages
with open("user_messages.txt", "r") as f:
    messages = f.read()

st.subheader("User Messages (30)")
st.text(messages)

# MEMORY EXTRACTION
st.subheader("Step 1: Extract Memory")

if st.button("Extract Memory"):
    memory = extract_memory(messages, client)
    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)
    st.success("Memory extracted!")
    st.json(memory)

# Load existing memory if exists
try:
    with open("memory.json", "r") as f:
        memory = json.load(f)
except:
    memory = None

# PERSONALITY TESTING
st.subheader("Step 2: Test Persona Responses")

user_msg = st.text_input("Enter a user message:")

persona = st.selectbox(
    "Choose a persona:",
    ["Calm Mentor", "Witty Friend", "Therapist-Style", "Professional Coach"]
)

if st.button("Generate Responses"):
    if memory is None:
        st.error("Please extract memory first.")
    else:
        baseline = baseline_reply(user_msg, memory, client)
        persona_out = persona_reply(user_msg, persona, memory, client)

        st.write("### Baseline Response")
        st.info(baseline)

        st.write("### Persona Response")
        st.success(persona_out["reply"])

        st.write("### Persona Used")
        st.code(persona_out["persona_used"])

# DOWNLOAD memory.json
if memory:
    st.download_button(
        "Download memory.json",
        json.dumps(memory),
        file_name="memory.json"
    )
