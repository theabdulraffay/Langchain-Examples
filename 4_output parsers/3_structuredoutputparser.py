from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# it does enforce a schema 

load_dotenv()

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Write 3 facts about the topic: {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions(),
    },
)
# prompt = template.format(topic="black hole")

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(type(final_result))
# print(final_result)


chain  = template | model | parser
# all this can be done using chains

result = chain.invoke({"topic": "black hole"})
print(result)


# Data validation cannot be validate in this parser