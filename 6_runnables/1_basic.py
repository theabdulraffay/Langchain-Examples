import random
class NakliLLM:
    def __init__(self):
        print('LLm created')

    def predict(self, prompt):
        response_list = [
            "This is a fake response 1",
            "This is a fake response 2",
            "This is a fake response 3"       
        ]

        return {'response': random.choice(response_list)}


class NakliPromptTemplate:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)
    


class NakliLLMChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt
    
    def run(self, input_dict):
        formatted_prompt = self.prompt.format(input_dict)
        response = self.llm.predict(formatted_prompt)
        return response['response']


llm = NakliLLM()
# print(llm.predict("What is the capital of India?"))

template = NakliPromptTemplate(
    template='Write a {length} note on {topic}',
    input_variables=['topic', 'length']
)

# formatted_prompt = template.format({'topic': 'India', 'length': 'large'})
# print(formatted_prompt)



chain = NakliLLMChain(llm=llm, prompt=template)
result = chain.run({'topic': 'India', 'length': 'large'})