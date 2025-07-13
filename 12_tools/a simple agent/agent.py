from langchain_core.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent, create_openai_tools_agent
load_dotenv()

@tool
def add(a: int, b: int) -> int:
    """Adds two numbers."""

    print('i was called')
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b

@tool
def square(a: int) -> int:
    """Squares a number."""
    return a * a

tools = [add, multiply, square]

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
          You are a mathematical assistant. Use your tools to answer questions. Whatever the tool returns never change the output. and display the output as it is.
          If you do not have a tool to answer the question, say so. 
        
          Return only the answers. e.g
          Human: What is 1 + 1?
          AI: 2
          """),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)

agent = create_tool_calling_agent(llm= model,tools=tools, prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

result = agent_executor.invoke({
    "input": "What is the square of (5 + 11 * 2)?",
})

print(result['output'])