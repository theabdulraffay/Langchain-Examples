from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4")
# temprature sets the randomness of the model's responses, 
# 0 - 0.3 is more deterministic, 0.7 - 1.0 is more creative/ writings.
llm.temperature = 0.7

# max_completion_token sets the maximum number of tokens in the response.
llm.max_completion_tokens = 10

result = llm.invoke("What is the capital of France?")
print(result)
print(result.content)
# Output: The capital of France is Paris.
# This code will not run as there is not an OpenAI API key set in the environment variables.
# Note: Make sure to set the OPENAI_API_KEY in your environment variables before running this code.