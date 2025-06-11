from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=15,
)


# Types of messages in LangChain that will store the conversation history
# messages = [
#     SystemMessage(
#         content="You are a helpful assistant"
#     ),
#     HumanMessage(
#         content='Tell me about language models and their applications in natural language processing.'
#     )
# ]

# response = model.invoke(messages)
# messages.append( AIMessage(content=response.content))
# print(f"AI: {messages}")\






chat_history = [
    SystemMessage(content="You are a helpful assistant"),
] # This will store the conversation history

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break

    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"Chatbot: {response.content}")

print(f"Chat history: {chat_history}")