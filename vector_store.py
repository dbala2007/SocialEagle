from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

texts = [
    "Python is a programming language",
    "Streamlit is used to build web apps",
    "Dogs are friendly animals",
    "Cats like to sleep a lot"
]

embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

print("Ready")

vector_store = FAISS.from_texts(texts=texts, embedding=embeddings)
print("All texts are stored in the vector store")

query = "tell me about pets"

results = vector_store.similarity_search(query=query, k=2) #k=2 top 2 matches

print("Top matches for: ", query)
for r in results:
    print("- ", r.page_content)

#to store it in local vector DB
# vector_store.save_local("my_vector_store")

#To load local vector DB
#vector_store = FAISS.load_local("my_vector_store", embeddings, allow_dangerous_deserialization=True)

retriever = vector_store.as_retriever(search_kwargs={'k': 2}) #return top2 results
print("Retriever is ready")

question = "What is used to build web apps?"

results2 = retriever.invoke(question)

print("Question: ", question)
print("Relevant information found")
for r in results2:
    print("- ", r.page_content)