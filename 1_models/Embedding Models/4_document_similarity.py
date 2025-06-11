from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
# from dotenv import load_dotenv
import os


os.environ['HF_HOME'] = 'C:\\Agentic AI'  # This is where the HuggingFace models will be downloaded and cached.

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32) # Uncomment this line to use OpenAI embeddings instead of HuggingFace embeddings
# load_dotenv()
# again we need to set the environment variable OPENAI_API_KEY in the .env file


documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers.",
    "Bumrah has been a key player for India in all formats of the game.",
]

query = 'Who is bumrah'

documents_embeddings = embedding.embed_documents(documents)  # Embedding multiple documents
query_embedding = embedding.embed_query(query)  # Single query embedding

# print(documents_embeddings)
# print(query_embedding)

scores = cosine_similarity([query_embedding], documents_embeddings)[0]
print(scores)
# Get the index of the document with the highest score


index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)

