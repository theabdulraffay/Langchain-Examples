from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ['HF_HOME'] = 'C:\\Agentic AI'  # This is where the HuggingFace models will be downloaded and cached.
# If the model is not downloaded, it will be downloaded to this location and run locally on the PC.
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", )

text = "Islamabad is the capital of Pakistan."

embedding_result = embedding.embed_query(text)  # Single query embedding
# it will give 384 dimensions of embedding for the text

# this will return a list of floats representing the embedding of the query
# print(str(embedding_result))



documents = [
    "Islamabad is the capital of Pakistan.",
    "The capital of France is Paris.",
    "Tokyo is the capital of Japan.",
    "Washington, D.C. is the capital of the United States.",
    "Canberra is the capital of Australia."
]

result = embedding.embed_documents(documents)  # Embedding multiple documents

# this will return a list of lists, where each inner list is the embedding of a document
print(result)
