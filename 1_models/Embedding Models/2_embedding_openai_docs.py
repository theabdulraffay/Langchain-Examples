from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

# again we need to set the environment variable OPENAI_API_KEY in the .env file

documents = [
    "Islamabad is the capital of Pakistan.",
    "The capital of France is Paris.",
    "Tokyo is the capital of Japan.",
    "Washington, D.C. is the capital of the United States.",
    "Canberra is the capital of Australia."
]

result = embedding.embed_documents(documents)  # Embedding multiple documents
# this will return a list of lists, where each inner list is the embedding of a document
print(str(result))