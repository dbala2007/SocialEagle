# #create a sample file to load
# text = """
# LangChain is a framework for building AI apps.
# It helps connect language models with your own data.
# RAG means Retrieval Augmented Generation.
# """

# with open("sample.txt", "w") as f:
#     f.write(text)

# print("sample.txt created")

# from langchain_community.document_loaders import TextLoader

# loader = TextLoader("sample.txt")
# documents = loader.load()

# print("Number of documents: ", len(documents))
# print("Content")
# print(documents[0].page_content)

#TextLoader - .txt
#PyPDFLoader - .pdf (pypdf prerequisite)
#CSVLoader - .csv
#WebBaseLoader - Web scraping

#Step2 - Text Splitter

# long_text = """
# Python is a programming language. It is easy to learn.
# Streamlit is used to build web apps. LangChain helpds build AI apps.
# RAG combines search with AI models. Embeddings turn text into numbers.
# Vector stores save those numbers. Retrievers find the matches
# """

# print("Total characters: ",len(long_text))

# from langchain_text_splitters import RecursiveCharacterTextSplitter

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=80,
#     chunk_overlap=20
# )

# chunks = splitter.split_text(long_text)

# print("Number of chunks: ", len(chunks))
# for i, chunk in enumerate(chunks):
#     print(f"\nChunk: {i+1}: ")
#     print(chunk)

#Embeddings

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
print("Embedding is ready")

from langchain_openai import OpenAIEmbeddings

openai_embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

print("Open AI embedding is ready")

text = "I love programming in python"

opensource_vector = embeddings.embed_query(text)
print("How many numbers in this vector?: ", len(opensource_vector))
print("First 5 numbers: ", opensource_vector[:5])

openai_vector = openai_embeddings.embed_query(text)
print("How many numbers in this vector?: ", len(openai_vector))
print("First 5 numbers: ", openai_vector[:5])