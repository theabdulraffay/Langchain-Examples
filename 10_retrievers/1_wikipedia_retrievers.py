from langchain_community.retrievers import WikipediaRetriever

# it is working as a search engine thatswhy it is not a document loader but a retriever 
retriever = WikipediaRetriever(
    top_k_results=2,
    language="en",
)

query = "What is the capital of Pakistan?"

docs = retriever.invoke(query)

# print(f"Query: {query}")

# Print retrieved content
for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...")  # truncate for display