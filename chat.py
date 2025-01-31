import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
import ollama
import re
import shelve

current_model = "deepseek-r1:8b" # ollama model being used

# query validation from user to block unrelated responses.
import re

def validate_query(query):
    # converting to lower case for better matching
    query_lower = query.lower()

    # keywords to check for for validation
    financial_keywords = [
        "finance", "money", "budget", "invest", "savings", "spending",
        "tax", "tfsa", "rrsp", "stocks", "bonds", "interest rate",
        "credit", "debt", "loan", "mortgage", "retirement", "dividends",
        "income", "expenses", "saving", "budgeting", "monthly spending", "cash flow"
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


def chat_with_bot(question):
    # validate the query to improve inference
    if not validate_query(question):
        humor_responses = [
            "Oops! Looks like I got lost in the financial world. Let's talk about savings instead! 😅",
            "I may not know much about that, but I can definitely help you with budgeting your coffee budget! ☕️💰",
            "Not my area of expertise, but I bet your financial future will thank you if you start saving now! 💸",
            "I am afraid I only speak the language of money... but feel free to ask me about it! 💬💰"
        ]
        return humor_responses[hash(question) % len(humor_responses)]  # randomize humorous responses to make it feel less restrictive

    formatted_prompt = prompt.format(question=question)

    # getting response from the local ollama model
    response = ollama.chat(
        model=current_model,
        messages=[{"role": "user", "content": formatted_prompt}]
    )

    # Print the raw response for debugging purposes
    print(response)

    # Extract raw content and clean it up
    raw_content = response.get("message", {}).get("content", "")
    
    # Clean up the response to remove <think> tags and other unnecessary elements
    clean_content = re.sub(r'<think>.*?</think>', '', raw_content, flags=re.DOTALL)  # remove content inside <think> tags
    clean_content = re.sub(r'<.*?>', '', clean_content)  # remove any remaining HTML tags
    
    return clean_content.strip() if clean_content else "Error: No content available after cleaning."





# streamlit title and strat message 
st.title("Financial Advisor Chatbot 💰")
st.write("Ask me anything about budgeting, saving, or investing. Type '/quit' to exit.")

# function to load and save chat history from shelve
def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])

# function to save chat_history
def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages

# initializting  or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

# slidebar to delete chat history
with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])

# displays chat history
for message in st.session_state.messages:
    avatar = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# chat interface
if prompt := st.chat_input("How can I help?"):
    # adds user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # gets response from chatbot
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        full_response = ""
        
        # gets the response from the Ollama model
        response = chat_with_bot(prompt)  # Use the function to get response

        # displays the response from model
        message_placeholder.markdown(response)
    
    # adds assistants response to history
    st.session_state.messages.append({"role": "assistant", "content": response})

# saves chat history after each interaction
save_chat_history(st.session_state.messages)