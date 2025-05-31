from langchain_core.prompts  import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq


chat_template = ChatPromptTemplate(
    [
        ('system', 'You are a helpful {domain} expert'),
        ('human', 'Explain in simple words what is {topic}')
        # SystemMessage(
        #     content = 'You are a helpful {domain} expert'
        # ),
        # HumanMessage(
        #     content = 'Explain in simple words what is {topic}'
        # )
    ]
)


prompt = chat_template.invoke(
    {
        'domain': 'Photography',
        'topic': 'Rule of third'
    }
)