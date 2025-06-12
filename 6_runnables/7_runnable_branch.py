#  it take care of conditional calls 

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers  import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableBranch

load_dotenv()

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a detail report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

report_generate_chain = RunnableSequence(prompt, model, parser)

# if the report of greater than 500 words ti will transfer the text to the prompt2

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500 , RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_generate_chain, branch_chain)
result = final_chain.invoke({
    'topic' : 'Russia vs Ukarine'
})

print(result)

# if you want to use RunnableSequence we can also use it using the pipe operator it is called LCEL