from langchain_core.tools import tool, Tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import requests 
from langchain_community.tools import DuckDuckGoSearchRun
from ddgs import DDGS
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain_community.utilities import SearchApiAPIWrapper
import os




load_dotenv()

search_tool = DuckDuckGoSearchRun()
searching_tool = DDGS()
search = SearchApiAPIWrapper()
print(type(search))

@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """

  key = os.getenv('WEATHERSTACK_API')
#   print(key)
  url = f'https://api.weatherstack.com/current?access_key={key}&query={city}'

  response = requests.get(url)

  return response.json()

tool = Tool(
    name="search",
    func=search.run,
    description="A tool to search the web for information. Input should be a search query."
)

search_custom_tool = Tool(
    name="search_tool",
    func=searching_tool.text,
    description="A tool to search the web for information. Input should be a search query."
)
# print(search.run('top news headlines'))

# print(search_tool.invoke('top news headlines'))
# print(searching_tool.text('top news headlines'))

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# pull the react prompt from langchain hub
react_prompt = hub.pull("hwchase17/react") #pull the standard react agent prompt from langchain hub


agent = create_react_agent(
    llm=model,
    prompt=react_prompt,
    tools=[tool, get_weather_data]
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[tool, get_weather_data],
    verbose=True,
    # max_iterations=3,  # limit the number of iterations
    # return_intermediate_steps=True  # return intermediate steps for debugging

)

response = agent_executor.invoke({'input':'What is the capital of Pakistan? whats the weather there?'})
print(response['output'])

# print(get_weather_data.invoke('Karachi'))