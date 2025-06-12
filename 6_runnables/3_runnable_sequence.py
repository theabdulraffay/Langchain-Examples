# it connects 2 runnables in sequence by formming a chain
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers  import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence


load_dotenv()

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt = PromptTemplate(
    template='Write a joke about {joke}',
    input_variables=[
        'joke'
    ]
)


prompt2 = PromptTemplate(
    template='Exxplain the following {joke}',
    input_variables=[
        'joke'
    ]
)

parser= StrOutputParser()

chain = RunnableSequence(
    prompt, model, parser, prompt2, model, parser
)

result = chain.invoke({
    'joke' : 'AI'
})

print(result)