# it will analyze feedback if its positive it will give positive response and vice versa

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableBranch, RunnableLambda

# data validation and schema enforcement using PydanticOutputParser

load_dotenv()

# model = ChatGroq(
#     model="meta-llama/llama-4-maverick-17b-128e-instruct",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
# )
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-8b",
    temperature=0,
    max_tokens=None,
    max_retries=2,
)

string_parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the field')


parser = PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template="Classify the statement of the following feedback text into positive or negative \n {text} \n {format_instructions}",
    input_variables=["text"],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)


classifier_chain = prompt1 | model | parser

# result = chassifier_chain.invoke({'text' : 'This is a terrible smart phone'})

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)


prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)


branch_chain = RunnableBranch(
    # (condition, chain)
    (lambda x:x.sentiment == 'positive', prompt2 | model | string_parser), 
    (lambda x:x.sentiment == 'negative', prompt3 | model | string_parser), 
    RunnableLambda(lambda x: "could not find statement")

)


chain = classifier_chain | branch_chain

result = chain.invoke({'text' : 'This is a terrible phone'})

print(result)
chain.get_graph().print_ascii()