# import fitz  # PyMuPDF
from PIL import Image
import pytesseract
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pdf2image import convert_from_path
import xml.etree.ElementTree as ET
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings()
text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )


# def detect_pdf_type(pdf_path):
#     doc = fitz.open(pdf_path)
#     page = doc[0]
    
#     # Check if text is extractable
#     text = page.get_text()
#     if len(text.strip()) > 50:  # Threshold for meaningful text
#         return "text_based"
    
#     # Check if it contains images (likely scanned)
#     image_list = page.get_images()
#     if image_list:
#         return "scanned"
    
#     # Check for XML structure
#     if text.startswith("<?xml") or "<xml" in text:
#         return "xml"
    
#     return "unknown"

# def extract_text_pdf(pdf_path):
#     loader = PyPDFLoader(pdf_path)
#     pages = loader.load()
#     return pages

def extract_scanned_pdf(pdf_path):
    # Convert PDF to images
    images = convert_from_path(pdf_path= pdf_path, poppler_path=r"C:\Users\Abdul Raffay\Downloads\Release-25.07.0-0\poppler-25.07.0\Library\bin")
    
    extracted_text = []
    for i, image in enumerate(images):
        # Apply OCR
        text = pytesseract.image_to_string(image, lang='eng')
        extracted_text.append({
            'page': i + 1,
            'content': text,
            'metadata': {'source': pdf_path, 'page': i + 1}
        })
    
    return extracted_text

# def extract_xml_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     xml_content = ""
    
#     for page in doc:
#         xml_content += page.get_text()
    
#     # Parse XML
#     try:
#         root = ET.fromstring(xml_content)
#         # Extract structured data based on your XML schema
#         return parse_xml_structure(root)
#     except ET.ParseError:
#         # Fallback to text extraction
#         return [{'content': xml_content, 'metadata': {'source': pdf_path}}]
    

# def process_pdf(pdf_path):
#         pdf_type = detect_pdf_type(pdf_path)
        
#         if pdf_type == "text_based":
#             documents = extract_text_pdf(pdf_path)
#         elif pdf_type == "scanned":
#             raw_data = extract_scanned_pdf(pdf_path)  # or use EasyOCR/PaddleOCR
#             documents = [Document(page_content=item['content'], 
#                                 metadata=item['metadata']) for item in raw_data]
#         elif pdf_type == "xml":
#             raw_data = extract_xml_pdf(pdf_path)
#             documents = [Document(page_content=item['content'], 
#                                 metadata=item['metadata']) for item in raw_data]
#         else:
#             # Fallback strategy
#             documents = extract_text_pdf(pdf_path)
        
#         # Split documents into chunks
#         split_docs = text_splitter.split_documents(documents)
        
#         return split_docs
    
# def create_vectorstore(all_documents):
#     vectorstore = FAISS.from_documents(all_documents, embeddings)
#     return vectorstore


test = extract_scanned_pdf("companies_house_document.pdf")
print(test)