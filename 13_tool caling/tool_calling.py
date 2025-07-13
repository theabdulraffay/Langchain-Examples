from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

# tool create

@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b


# bind tool 

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# tool binding 
llm_with_tools = model.bind_tools([multiply])

# tool calling
# llm doesnot run the tool call it just suggest the tool call, it is run by the agent executor


messages = [
  HumanMessage(
    content="can you multiply 2 and 3?"
  )
]

res = llm_with_tools.invoke('can you multiply 2 and 3?')

messages.append(res)

result = multiply.invoke(
  res.tool_calls[0]
)

messages.append(result)

print(result)
print(messages)

# tool creation-> tool binding -> tool calling -> tool execution
# step where the actual tool is called and executed and inputs are given based on llm suggestion
