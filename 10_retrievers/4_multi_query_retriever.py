# sometimes a single query is not enough to retrieve relevant documents. In such cases, we can use multiple queries to retrieve more relevant documents.
# it tries to remoe ambiguity in the query by using multiple queries to retrieve relevant documents.
# it first send the query to an LLM to generate multiple queries, then it uses those queries to retrieve relevant documents from the vector store. 


from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever
