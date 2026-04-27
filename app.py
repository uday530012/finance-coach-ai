import streamlit as st
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

# Load model
llm = Ollama(model="llama3")

# Clean prompt
prompt = PromptTemplate.from_template("""
You are a professional Indian financial advisor.

STRICT INSTRUCTIONS:
- Output ONLY a clean table
- No extra text
- No crypto

Format:
Category | Amount (Rs) | Reason
--------------------------------

Salary: {salary}
Tone: {tone}
""")

chain = prompt | llm

# UI
st.set_page_config(page_title="Finance Coach", page_icon="💰")

st.title("💰 Personal Finance Coach")
st.write("Get your monthly budget plan instantly")

salary = st.text_input("Enter your monthly salary")
tone = st.selectbox("Select tone", ["strict", "friendly"])

if st.button("Generate Plan"):
    if salary:
        result = chain.invoke({
            "salary": salary,
            "tone": tone
        })
        st.subheader("📊 Your Budget Plan")
        st.code(result)
    else:
        st.warning("Please enter salary")