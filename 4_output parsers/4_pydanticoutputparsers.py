from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI

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

# it does enforce a schema 
# Data validation can be done using PydanticOutputParser, which is a subclass of StructuredOutputParser.


class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person", gt=18)
    city: str = Field(description="City where the person lives")



parse = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="generate name, age and city of a fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables={
        "format_instruction": parse.get_format_instructions(),
    },
)

# prompt = template.format(place="Indian")
# # print(f"Prompt: {prompt}")
# result = model.invoke(prompt)
# final_result = parse.parse(result.content)
# print(type(final_result))
# print(final_result)
# print(result.content)


chain = template | model | parse
result = chain.invoke({"place": "Indian"}) 
print(result)
print(type(result))