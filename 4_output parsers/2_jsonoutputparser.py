from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# it doesnot enforce a schema 

load_dotenv()

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

parser = JsonOutputParser()

template = PromptTemplate(
    template= "Give me the name, age and city of a fictional person \n {format_instructions}",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions(),
    },
)

#all this can be done using chains
# prompt = template.format()

# print(f"Prompt: {prompt}")

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(type(final_result))
# print(final_result)

chain = template | model | parser
result = chain.invoke({})
print(result)
