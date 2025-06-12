# It help us to form parallel chains, at the same time it will execute 2 models for the response, all chains will get single input but output is different from each, because there will be multiple chains executing at the same time (in parallel)

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers  import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,  RunnableParallel

load_dotenv()

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)


prompt2 = PromptTemplate(
    template='Generate a linked post about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chains = RunnableParallel(
    {
        'tweet' : RunnableSequence(prompt1, model, parser),
        'linkedin' : RunnableSequence(prompt2, model, parser),
    }
)


# result = parallel_chains.invoke({
#     'topic' : 'AI'
# })

# print(result)

parallel_chains.get_graph().print_ascii()