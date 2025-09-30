import pytesseract
from pdf2image import convert_from_path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List, TypedDict, Annotated, Optional, Literal
from langchain_community.document_loaders import PyPDFLoader
load_dotenv()



llm = ChatOpenAI(model="gpt-4")

class TotalEmployees(BaseModel):
    
    total_number_of_employees: int = Field(description='"The total number of employees" for the latest year')

structuredLlm = llm.with_structured_output(TotalEmployees)

def extract_scanned_pdf(pdf_path):
    # Convert PDF to images
    images = convert_from_path(pdf_path= pdf_path, poppler_path=r"C:\Users\Abdul Raffay\Downloads\Release-25.07.0-0\poppler-25.07.0\Library\bin")
    
    extracted_text = []
    for i, image in enumerate(images):
        # Apply OCR
        text = pytesseract.image_to_string(image, lang='eng')
        if 'average monthly number of persons' in text:
            extracted_text.append({
            'page': i + 1,
            'content': text,
            'metadata': {'source': pdf_path, 'page': i + 1}
        })
    
    return extracted_text

def model(text: List[str]):
    response = structuredLlm.invoke(f'I will provide you with extracted text of a pdf and you have to find "The total number of employees" from that text, make sure you give me number for the latest year, if you cannot find the total number simple say you cannot find it \n NEVER add information from yourself, keep your answer as short as possible\n This is the text {text}')

    return response


def extract_text_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    return pages
text = extract_scanned_pdf('companies_house_document.pdf')
response = model(text)

print(response)
print(response.total_number_of_employees)



