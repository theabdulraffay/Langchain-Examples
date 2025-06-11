from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# template
chat_template = ChatPromptTemplate([
    ('system', 'You are a good friend that listen to people queries and provide short helpful responses that donot exceed 100 words.'),
    MessagesPlaceholder(variable_name = "chat_history"),
    # ('human', MessagesPlaceholder(variable_name="chat_history")),
    ('human', '{query}'),
])




chat_history = []
# load chat history
with open('chat_history.txt') as f:
    for line in f:
        line = line.strip()
        if line.startswith("User: "):
            # Remove the prefix and create a HumanMessage
            content = line[len("User: "):]
            chat_history.append(HumanMessage(content=content))
        elif line.startswith("AI: "):
            # Remove the prefix and create an AIMessage
            content = line[len("AI: "):]
            chat_history.append(AIMessage(content=content))

# print(f"Chat history: {chat_history}")

# creatre prompt

# prompt = chat_template.invoke(
#     {
#         'chat_history': chat_history,
#         'query': 'What is the status of my order?'
#     }
# )

# print(f"Prompt: {prompt}")

# invoke model

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=100,
)
# response = model.invoke(prompt)
# print(f"Response: {response.content}")
# # Append the response to chat history
# chat_history.append(AIMessage(content=response.content))
# # Save the updated chat history
# with open('chat_history.txt', 'a') as f:
#     single_line_content = response.content.replace('\n', ' ')
#     f.write(f"AI: {single_line_content}\n")





while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break

    with open('chat_history.txt', 'a') as f:
        single_line_content = user_input.replace('\n', ' ')
        f.write(f"User: {single_line_content}\n")

    prompt = chat_template.invoke(
        {
            'chat_history': chat_history,
            'query': user_input
        }
    )

    response = model.invoke(prompt)
    chat_history.append(AIMessage(content=response.content))
    print(f"Chatbot: {response.content}")

# Save the updated chat history
    with open('chat_history.txt', 'a') as f:
        single_line_content = response.content.replace('\n', ' ')
        f.write(f"AI: {single_line_content}\n")