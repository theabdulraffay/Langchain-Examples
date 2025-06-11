from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# llm = HuggingFaceEndpoint(
#     repo_id="google/gemma-2-2b-it",
#     task="text-generation",
# )

# model = ChatHuggingFace(llm= llm)

# 1st prompt template
template1 = PromptTemplate(
    template="Write a detail report on the following topic: {topic}",
    input_variables=["topic"],
)


# 2nd prompt template
template2 = PromptTemplate(
    template="Write a 5 line summary of the following report: {report}",
    input_variables=["report"],
)

# This is all without using the string output parser
# prompt1 = template1.invoke({"topic": "black hole"})
# result = model.invoke(prompt1)
# prompt2 = template2.invoke({"report": result.content})
# result2 = model.invoke(prompt2)
# print(result.content)
# print(result2.content)




# This is using the string output parser

parser = StrOutputParser()
# this is the entire flow of the code
# parser will automatically extract result.content from the model response
chain = template1 |model | parser | template2 | model | parser

# invoke the chain
result = chain.invoke({"topic": "black hole"})
print(result)