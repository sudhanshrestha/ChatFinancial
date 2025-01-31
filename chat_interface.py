from langchain_core.prompts import ChatPromptTemplate
import ollama
import subprocess
import time
import re
import requests


currrent_model = "deepseek-r1:1.5b" # ollama model being used
# # Function to check if Ollama is running
# def is_ollama_running():
#     try:
#         response = requests.get("http://localhost:11434/api/tags", timeout=3)
#         return print("OK..")
#     except requests.ConnectionError:
#         return False

# # Start Ollama if not running
# if not is_ollama_running():
#     print("🔄 Starting Ollama server...")
#     subprocess.Popen("ollama serve", shell=True)
#     time.sleep(5)  # Wait a few seconds to let the server start



# query validation from user to block unrelated responses.
import re

def validate_query(query):
    # converting to lower case for better matching
    query_lower = query.lower()

    # keywords to check for for validation
    financial_keywords = [
        "finance", "money", "budget", "invest", "savings", "spending",
        "tax", "tfsa", "rrsp", "stocks", "bonds", "interest rate",
        "credit", "debt", "loan", "mortgage", "retirement", "dividends"
    ]

    # checking if any keyword is in the query
    for keyword in financial_keywords:
        if re.search(rf"\b{keyword}\b", query_lower):  # \b ensures whole words
            return True

    return False


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

# function for chat responses
def chat_with_bot(question):
    # Validate query
    if not validate_query(question):
        return "I am designed to provide financial advice only. Please ask a financial-related question."

    formatted_prompt = prompt.format(question=question)

    # Get response from Ollama model
    response = ollama.chat(
        model= currrent_model, # can changet the model to any model from ollama that you want
        messages=[{"role": "user", "content": formatted_prompt}]
    )
    
    return response["message"]["content"]

# Welcome message
print("Hello! I am a Financial Advisor Chatbot! 💰")
print("Ask me anything about budgeting, saving, or investing. Type '/quit' to exit.\n")

# Chat loop
while True:
    query = input("You: ")
    if query.strip().lower() == "/quit":
        print("Chatbot: Goodbye! Stay financially wise! 💸")
        break

    answer = chat_with_bot(query)
    print("Chatbot:", answer)
