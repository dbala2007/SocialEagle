from pathlib import Path
from langchain_community.vectorstores import FAISS

from load_document import load_scheme_documents
from chunk_documents import split_documents
from embedding_factory import get_embeddings
from settings import Settings

VECTOR_STORE = Path(Settings.VECTOR_STORE_PATH)

def build_vector_store(chunks):
    embeddings = get_embeddings()

    return FAISS.from_documents(
        chunks,
        embeddings
    )

def create_vector_store():
    documents = load_scheme_documents(Settings.DATA_PATH)
    chunks = split_documents(documents)

    vector_store = build_vector_store(chunks)

    VECTOR_STORE.mkdir(exist_ok=False)

    vector_store.save_local(
        str(VECTOR_STORE)
    )

    print("Vector store saved successfully")

if __name__ == "__main__":
    create_vector_store()