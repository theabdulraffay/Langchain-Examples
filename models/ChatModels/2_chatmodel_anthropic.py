from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model_name= "claude-3-5-sonnet-20241022")

result = model.invoke("What is the capital of France?")  # Example usage

#Add ANTHROPIC_API_KEY to your .env file
#As api key is paid so I havent added it here
print(result.content)