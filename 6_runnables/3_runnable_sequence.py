# it connects 2 runnables in sequence by formming a chain
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers  import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence


load_dotenv()

prompt = PromptTemplate(
    template='Write a joke about {joke}',
    input_variables=[
        'joke'
    ]
)

