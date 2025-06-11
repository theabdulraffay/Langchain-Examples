from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

# again it will use HUGGINGFACEHUB_API_TOKEN from .env file
# https://huggingface.co/settings/tokens to get api key

model = ChatHuggingFace(llm=llm)


try:
    result = model.invoke("What is the capital of India")

    print(result.content)
except Exception as e:
    print(f"Error: {e}")