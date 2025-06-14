# it give a list of document, each doc is a page of the pdf we provided, so easch page is divided into a single document
# also pdf_loader is not great with scanned pdf and complex layouts

# PDFPlumberLoader (tables and colums), AmazonTextractPDFLoader (scanned immages pdf), PyMuPDFLoader (layout and image data pdf), UnstructuredPDFLoader

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path='dl-curriculum.pdf')

docs = loader.load()

print(docs[0].metadata)