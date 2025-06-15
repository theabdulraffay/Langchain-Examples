# Divide text to a certain length or token, it divide using the length or token -> most simplest  

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""


splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0, # it shows the over lapping region between 2 splits
    separator=''
)

loader = PyPDFLoader(file_path='dl-curriculum.pdf')

docs = loader.load()

result = splitter.split_documents(docs)

# split_text = splitter.split_text(text)
# print(split_text)

print(result)
# print()