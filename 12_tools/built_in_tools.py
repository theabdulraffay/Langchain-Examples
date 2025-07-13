from langchain_community.tools import DuckDuckGoSearchResults, DuckDuckGoSearchRun
from ddgs import DDGS
from langchain_community.tools import ShellTool

search_tool = DuckDuckGoSearchResults()

another_search_tool = DDGS()

print(another_search_tool.text('top news'))
print(search_tool.invoke('who is Demis Hassabis'))



shell = ShellTool()
response = shell.invoke('mkdir file')
