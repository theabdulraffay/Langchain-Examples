from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=1000,
)

chat_history = [] # This will store the conversation history

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.lower() == "exit":
        break

    response = model.invoke(chat_history)
    chat_history.append(response.content)
    print(f"Chatbot: {response.content}")

print(f"Chat history: {chat_history}")