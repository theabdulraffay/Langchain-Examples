

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


# when the directory contains all the same type of file, in this case it is pdfs
loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# this load() function will load all the files in the directory which gets heavy for the memory in case of many documents in the directory or large pdf

docs = loader.load()

# Not all teh document are loaded at once, they are fetched once at a time as needed,
# load() works by fetching all the data and then using it therefore increasing time, lazy_load() works by fetching the doc implment the usage delete from the memory and then the next doc is fetched in the memory. 

doc = loader.lazy_load()
print(len(docs))
print(len(doc))