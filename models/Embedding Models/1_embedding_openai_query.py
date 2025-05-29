from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

# again we need to set the environment variable OPENAI_API_KEY in the .env file

embedding_result = embedding.embed_query("Islamabad is the capital of Pakistan.") # Single query embedding

# this will return a list of floats representing the embedding of the query
print(str(embedding_result))