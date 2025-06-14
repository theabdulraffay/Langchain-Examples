from langchain_community.document_loaders import TextLoader

loader = TextLoader(file_path="cricket.txt", encoding='utf-8')

docs = loader.load()

# print(docs)
print(type(docs[0]))
print(docs[0].metadata)
