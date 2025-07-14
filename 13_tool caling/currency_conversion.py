from langchain.tools import tool
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
import os
import requests
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.tools import InjectedToolArg
from typing import Annotated
import json
load_dotenv()


@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """Returns the currency conversion factor from a guven base curency to a target currency."""


    api_key = os.getenv("EXCHANGE_RATE_API")

    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}'

    response = requests.get(url)
    return response.json()

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float: # injectedtoolargs make the llm to set the value only when it get the output from a previous tool calling
    """Given a currency conversion rate this function calculate the target currency from a given base currency value"""
    return base_currency_value * conversion_rate


model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
llm_with_tools = model.bind_tools([get_conversion_factor, convert])

messages = [
    HumanMessage(
        'What is the conversion factor between INR and USD, and based on that can you convert 10 usd to inr'

    )
]

ai_message = llm_with_tools.invoke(messages)
print(ai_message.tool_calls)
messages.append(ai_message)

for tool_call in ai_message.tool_calls:
    # execute the first tool anda find teh value of conversion rate
    if tool_call['name'] == "get_conversion_factor":
        conversion_rate = get_conversion_factor.invoke(tool_call)
        messages.append(conversion_rate)
        rate = json.loads(conversion_rate.content)['conversion_rate']
    
    if tool_call['name'] == "convert":
        # execute the second tool and find the value of converted currency
        tool_call['args']['conversion_rate'] = rate  # inject the conversion rate into the tool call
        tool_message = convert.invoke(tool_call)
        messages.append(tool_message)
# print(get_conversion_factor.invoke({
#     "base_currency": "USD",
#     "target_currency": "PKR"
# }))

print(messages)
result = llm_with_tools.invoke(messages)
print(result.content)