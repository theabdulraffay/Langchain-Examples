from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
import os

os.environ['HF_HOME'] = 'C:\Agentic AI' # This is where the HuggingFace models will be downloaded and cached.

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
    task="text-generation", 
    pipeline_kwargs = dict(
        temperature = 0.7, 
        max_new_tokens = 100
    )
)
model = ChatHuggingFace(llm = llm, model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

result = model.invoke("What is the capital of India?")
print(result)