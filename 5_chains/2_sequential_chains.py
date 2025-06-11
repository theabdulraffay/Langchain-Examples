from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt1 = PromptTemplate(

    template="Generate a detail report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate 5 line summary about the following text {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

# result = chain.invoke({"topic": "Block Chain Technology"})
# print(result)
chain.get_graph().print_ascii()