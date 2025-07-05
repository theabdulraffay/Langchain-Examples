from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv 
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_community.vectorstores import FAISS 
import os

from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()
os.environ['HF_HOME'] = 'C:\\Agentic AI'
model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
parser = StrOutputParser()


def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", )

vectorstore = FAISS.load_local("youtube_vectorstore", embedding, allow_dangerous_deserialization=True)

retriever = vectorstore.as_retriever(search_type = 'similarity',search_kwargs={"k": 4})


#  This chain will give us the context and question in parallel, which can be useful for RAG (Retrieval-Augmented Generation) tasks.
parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})

# query = parallel_chain.invoke('who is Demis')
prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)


main_chain = parallel_chain | prompt | model | parser

response = main_chain.invoke('is the topic of nuclear fusion discussed in this video? if yes then what was discussed')
print(response)

