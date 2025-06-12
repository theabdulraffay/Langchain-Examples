# it doesnot change any thing it just pass the input as it is in the output
#let say in a seq chain you want to see the output from the middle of the chian (which is not possible in seq chain) we use passthrought runnables

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers  import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,  RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

passthrought = RunnablePassthrough()


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

joke_generator_chain = RunnableSequence(prompt, model, parser)

#  In this code not onnly we will get the explanation but also the joke it self which was previously in the moddle of the chain
joke_and_explanation_chain = RunnableParallel(
    {
        'joke' : RunnablePassthrough(),
        'explanation' : RunnableSequence(prompt2, model, parser)
    }
)


final_chain = RunnableSequence(joke_generator_chain, joke_and_explanation_chain)
result = final_chain.invoke({
    'joke' : 'AI'
})

print(result)
