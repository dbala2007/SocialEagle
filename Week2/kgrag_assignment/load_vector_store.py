from pathlib import Path
from langchain_community.vectorstores import FAISS
from embedding_factory import get_embeddings
from settings import Settings

VECTOR_STORE_PATH = Path(Settings.VECTOR_STORE_PATH)

def load_vector_store() -> FAISS:
    """
    Load the persisted FAISS vector store.
    """

    embeddings = get_embeddings()

    vector_store = FAISS.load_local(
        folder_path=str(VECTOR_STORE_PATH),
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store