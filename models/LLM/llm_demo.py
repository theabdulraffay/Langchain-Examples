from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model= "gpt-3.5-turbo")


result = llm.invoke("What is the capital of France?")
print(result)
# Output: The capital of France is Paris.
# This code will not run as there is not an OpenAI API key set in the environment variables.
# Note: Make sure to set the OPENAI_API_KEY in your environment variables before running this code.