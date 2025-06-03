from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=50,
    timeout=None,
    max_retries=2,
)


class Review(TypedDict):
    summary: str
    sentiment: str



structured_model = model.with_structured_output(Review)

