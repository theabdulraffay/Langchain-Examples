from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

parser = StrOutputParser()

template = PromptTemplate(
    template='Write summary for the follwing {poem}',
    input_types=['poem']
)

loader = TextLoader(file_path="cricket.txt", encoding='utf-8')

docs = loader.load()

# All document contains 2 important things 1. metadata and 2. page content 

# print(docs)

chain = template | model | parser
print(type(docs[0]))
print(docs[0].metadata)
