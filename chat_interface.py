from langchain_core.prompts import ChatPromptTemplate
import ollama
import subprocess
import time
import re
import requests

# Function to check if Ollama is running
def is_ollama_running():
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=3)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

# Start Ollama if not running
if not is_ollama_running():
    print("🔄 Starting Ollama server...")
    subprocess.Popen("ollama serve", shell=True)
    time.sleep(5)  # Wait a few seconds to let the server start



# Custom query validator
def validate_query(query):
    allowed_keywords = ["financial", "income", "expense", "budget", "savings", "investment", "spending", "money"]
    return any(keyword in query.lower() for keyword in allowed_keywords)

# Prompt template
prompt_template = """
You are a financial advisor chatbot.
- If the user asks anything unrelated to financial topics, politely decline.
- Give personalized, number-driven financial advice.
- Keep responses concise and conversational.

User Question: {question}

Your response:
"""

prompt = ChatPromptTemplate.from_template(prompt_template)

# Function to handle chat input and response
def chat_with_bot(question):
    # Validate query
    if not validate_query(question):
        return "I am designed to provide financial advice only. Please ask a financial-related question."

    # Format input for the model
    formatted_prompt = prompt.format(question=question)

    # Get response from Ollama model
    response = ollama.chat(
        model="deepseek-r1:8b",
        messages=[{"role": "user", "content": formatted_prompt}]
    )
    
    model_res = response["message"]
    # If "<think>" appears, split and take only the final part
    if "<think>" in model_res and "</think>" in model_res:
        model_res = model_res.split("</think>")[-1].strip()

    return model_res

# Welcome message
print("💰 Welcome to the Financial Advisor Chatbot! 💰")
print("Ask me anything about budgeting, saving, or investing. Type '/quit' to exit.\n")

# Chat loop
while True:
    query = input("You: ")
    if query.strip().lower() == "/quit":
        print("Chatbot: Goodbye! Stay financially wise! 💸")
        break

    answer = chat_with_bot(query)
    print("Chatbot:", answer)
