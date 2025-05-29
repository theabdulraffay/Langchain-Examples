from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

# https://aistudio.google.com/apikey to get api key


model = ChatGoogleGenerativeAI(model ="gemini-1.5-flash-8b")
# Add GOOGLE_API_KEY to your .env file
result = model.invoke("What is the capital of France? also give the detail of the city")  # Example usage

print(result.content)

