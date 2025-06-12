# it allows custom function to apply in AI pipeline
 
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers  import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,  RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

def word_counter(text):
    return len(text.split())

# runnable_word_counter = RunnableLambda(word_counter)

# print(runnable_word_counter.invoke('Hi how are you'))

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

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'words': RunnableLambda(word_counter)
    }
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({
    'topic': 'AI'
    })