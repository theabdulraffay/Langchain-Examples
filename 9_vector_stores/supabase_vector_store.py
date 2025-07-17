from langchain_community.vectorstores import SupabaseVectorStore
import os
from dotenv import load_dotenv
from supabase.client import create_client, Client
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
load_dotenv()
os.environ['HF_HOME'] = 'C:\\Agentic AI'  # This is where the HuggingFace models will be downloaded and cached.
# If the model is not downloaded, it will be downloaded to this location and run locally on the PC.
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", )


supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_KEY")

print(supabase_key)
print(supabase_url)
supabase: Client = create_client(supabase_url, supabase_key)

# loader = TextLoader(file_path="cricket.txt", encoding='utf-8')
# loader = PyPDFLoader(file_path='dl-curriculum.pdf')

# documents = loader.load()

# print(len(documents))
# split = CharacterTextSplitter(chunk_size = 200, chunk_overlap = 10)

# docs = split.split_documents(documents)

# vector_store = SupabaseVectorStore.from_documents(
#     documents=documents,
#     embedding=embedding,
#     client = supabase,
#     table_name="documents"
# )


# print(len(docs))
# print(docs[0])


# vector_store = SupabaseVectorStore(
#     embedding=embedding,
#     client=supabase,
#     table_name="documents",
#     query_name="match_documents",
# )

# query = "what magic does cricket hold?"
# result = vector_store.similarity_search(query=query)

# retriever = vector_store.as_retriever(search_type='mmr')
# # another_result = retriever.invoke(query)
# print(result)
# print(another_result)

