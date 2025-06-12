import random
from abc import ABC, abstractmethod

class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        """
        Abstract method to be implemented by subclasses.
        This method should define how the runnable processes input data.
        """
        pass

class NakliLLM(Runnable):
    def __init__(self):
        print('LLm created')


    def invoke(self, prompt):
        response_list = [
            "This is a fake response 1",
            "This is a fake response 2",
            "This is a fake response 3"       
        ]

        return {'response': random.choice(response_list)}


    def predict(self, prompt):
        response_list = [
            "This is a fake response 1",
            "This is a fake response 2",
            "This is a fake response 3"       
        ]

        return {'response': random.choice(response_list)}


class NakliPromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables
    
    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)
    

class NakliStrParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data):
        """
        This is a placeholder for a string parser that would process the input data.
        For now, it simply returns the input data as is.
        """
        return input_data['response']


    

class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data) # This is using output of the previous runnable as input to the next
        return input_data
    

llm = NakliLLM()

template = NakliPromptTemplate(
    template='Write a {length} note on {topic}',
    input_variables=['topic', 'length']
)

parser= NakliStrParser()
chain = RunnableConnector(
    [
        template,
        llm,
        parser
    ]
)

result = chain.invoke({'topic': 'Pakistan', 'length': 'long'})
print(result)  # This will print the final response from the LLM after processing the input through the template
# Note: The above code is a simplified version of the original runnable components, focusing on the core functionality.
# Here I am making chains to form a larger components, now I will  take 2 large components to form a complex structure


#chain 1: input -> create joke
# chain 2: take joke -> give explanation\


template = NakliPromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

template2 = NakliPromptTemplate(
    template='Explain the following {joke}',
    input_variables=['joke']
)

# This will generate the joke
chain1 = RunnableConnector(
    [
        template, llm, parser
    ]
)

# This will give the explanation of the joke
chain2 = RunnableConnector(
    [
        template2, llm, parser
    ]
)

# This will merge the both chains
final_chain  = RunnableConnector(
    [
        chain1, chain2
    ]
)

result = chain1.invoke({
    'topic' : 'AI'
})

print(result)