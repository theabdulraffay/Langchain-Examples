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

parser = StrOutputParser()
prompt = PromptTemplate(
    template="Generate 5 intresting facts about {topic}"
    , input_variables=["topic"]
)

chain = prompt | model | parser

# result = chain.invoke({"topic": "India"})

# print(result)

chain.get_graph().draw_ascii()

