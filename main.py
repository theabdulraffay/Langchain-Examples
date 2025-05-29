from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq

load_dotenv()

# llm = ChatOpenAI(model="gpt-3.5-turbo")
# response = llm.invoke("What is the capital of France?") 
# print(response)


llm = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful assistant that help students with a clear road map for their desired career path.",
    ),
    ("human", "I want to learn flutter development."),
]
ai_msg = llm.invoke(messages)
with open("response.md", "w", encoding="utf-8") as f:
    f.write(ai_msg.content)
print(ai_msg.content)