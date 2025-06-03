from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field


load_dotenv()

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)



#Annotated TypeDict
# Annotated is a way to add metadata to the fields of a TypedDict, which can be useful for documentation or validation purposes. Here we use Annotated to provide additional information about each field in the TypedDict. 
#  we cannot add data validations to it
class ReviewWithAnnotation(BaseModel):
    
    key_themes: list[str] = Field(description= "Write down all the kety themes dicussed in the review, should be a list of strings.")
    summary: str = Field(description="The summary of the review, should be concise and to the point.")
    sentiment: Literal['positive', 'negative', 'neutral'] = Field(description="The sentiment of the review, should be either 'positive', 'negative', or 'neutral'.")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Name of the reviewer, if available.")

    
    # key_themes: Annotated[list[str], "Write down all the kety themes dicussed in the review, should be a list of strings."]
    # summary: Annotated[str, "The summary of the review, should be concise and to the point."]
    # sentiment: Annotated[str, "The sentiment of the review, should be either 'positive', 'negative', or 'neutral'."]
    # pros: Annotated[Optional[list[str]], "write down all the pros inside a list"]
    # cons: Annotated[Optional[list[str]], "write down all the cons inside a list"]




structured_model_with_annotation = model.with_structured_output(ReviewWithAnnotation)
result_with_annotation = structured_model_with_annotation.invoke("""
    I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

    The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

    However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

    Pros:
    Insanely powerful processor (great for gaming and productivity)
    Stunning 200MP camera with incredible zoom capabilities
    Long battery life with fast charging
    S-Pen support is unique and useful
                                    
    Review by Nitish Singh
""")



result_with_annotation = result_with_annotation.model_dump()  # Convert Pydantic model to dictionary


print(f"Type of result: {type(result_with_annotation)}") # This is  return a dictionary according to the TypedDict defined above
print(f"Key Themes: {result_with_annotation['key_themes']}")
print(f"Summary: {result_with_annotation['summary']}")
print(f"Sentiment: {result_with_annotation['sentiment']}")
print(f"Pros: {result_with_annotation['pros']}")
print(f"Cons: {result_with_annotation['cons']}")


