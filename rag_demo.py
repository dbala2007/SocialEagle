import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

#Question
question = "What is a token?"

#Step1 Load the file
loader = TextLoader("llm_document.txt", encoding="utf-8")
documents = loader.load()

#Step2 Split the text into small chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

#Step3 Embed using free model
embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

#Step4 Store the chunks in a FAISS vector store
vector_store = FAISS.from_documents(chunks, embeddings)

#Step5 Retreive the 3 most relevant chunks for the question
results = vector_store.similarity_search(question, k=3)
context = "\n\n".join(r.page_content for r in results)

#Step6 Answer the question using OpenAI
print("Question: ", question)

if os.getenv("OPENAI_API_KEY"):
    from openai import OpenAI
    from langsmith.wrappers import wrap_openai

    # client = OpenAI()
    client = wrap_openai(OpenAI())
    prompt = "Use ONLY this text: \n" + context + "\n\n Question: " + question

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{"role":"user", "content": prompt}]
    )

    print("\nAnswer")
    print(response.choices[0].message.content)
else:
    print("\nNo API  Key is set. Here is the RAG found: \n")
    print(context)