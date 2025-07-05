from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['HF_HOME'] = 'C:\\Agentic AI'  # This is where the HuggingFace models will be downloaded and cached.
# If the model is not downloaded, it will be downloaded to this location and run locally on the PC.

# video_id =  "Gfr50f6ZBvo"
# response = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])


# As it gives an list of dict so we will fijlter the text from the output
# transcript = " ".join(chunk["text"] for chunk in response)
# print(transcript)

# Split the transcript into chunks
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# chunks = text_splitter.create_documents([transcript])

# Create embeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", )
# vectorstore = FAISS.from_documents(chunks, embedding)

# Save the vectorstore to disk
# vectorstore.save_local("youtube_vectorstore")

vectorstore = FAISS.load_local("youtube_vectorstore", embedding, allow_dangerous_deserialization=True)

retriever = vectorstore.as_retriever(search_type = 'similarity',search_kwargs={"k": 4})

# data = retriever.invoke('What is deep mind')
# print(data)


model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)


question          = "is the topic of nuclear fusion discussed in this video? if yes then what was discussed"
retrieved_docs    = retriever.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

final_prompt = prompt.invoke({"context": context_text, "question": question})

answer = model.invoke(final_prompt)
print(answer.content)