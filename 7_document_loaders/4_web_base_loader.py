# it uses BeautifulSoup to extract data from a web page, for blogs news article where content is text usually 
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from bs4 import BeautifulSoup

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
    template='Answer the following question \n {question} from the following text \n {text}',
    input_variables=['question', 'text']
)


url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
# url = 'https://en.wikipedia.org/wiki/ChatGPT'
url2 = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421?pid=COMH64PY76CJKBYU&lid=LSTCOMH64PY76CJKBYUOL7TOK&marketplace=FLIPKART&sattr[]=color&sattr[]=system_memory&st=system_memory'
# url = 'https://www.amazon.com/ASUS-Display-NVIDIA%C2%AE-i7-13650HX-G614JV-AS74/dp/B0CRDCXRK2/ref=sr_1_1?_encoding=UTF8&sr=8-1'
loader = WebBaseLoader([url,url2])

docs = loader.load()

chain = template | model | parser

result = chain.invoke({
    'text' : docs[0].page_content,
    'question' : 'What is the discount price of the laptop, also tell me the model of the laptop'
})

# print(docs)
# print(docs[0].page_content)
# print(len(docs))
# soup = BeautifulSoup(docs[0].page_content, "html.parser")

# for tag in soup(["script", "style", "footer", "header", "nav", "noscript"]):
#     tag.decompose()

# clean_text = soup.get_text(separator=" ", strip=True)

# with open('response.txt', 'a', encoding='utf-8') as f:
#     f.write(clean_text)

print(result)