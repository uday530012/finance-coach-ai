from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

# Load local LLM
llm = Ollama(model="llama3")

# 🔥 Clean Prompt (Step-2 upgrade)
prompt = PromptTemplate.from_template("""
You are a professional Indian financial advisor.

STRICT INSTRUCTIONS:
- Output ONLY a clean table
- Do NOT include any introduction or explanation
- Do NOT use emotional language
- Do NOT add extra lines before or after

Format EXACTLY like this:
Category | Amount (Rs) | Reason
--------------------------------

Rules:
- No crypto investments
- Must include savings
- Should be practical for middle-class lifestyle

Salary: {salary}
Tone: {tone}
""")

# New LangChain style
chain = prompt | llm

# 👇 User input (Step-1 already added)
salary = input("Enter your monthly salary: ")
tone = input("Enter tone (strict / friendly): ")

# Generate response
response = chain.invoke({
    "salary": salary,
    "tone": tone
})

# Print output
print("\n📊 Budget Plan:\n")
print(response)