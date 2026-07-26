from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from settings import Settings

load_dotenv()

def get_embeddings():
    """
    Returns the embedding model.

    This factory makes it easy to replace
    OpenAI with Azure or HuggingFace later.
    """

    return OpenAIEmbeddings(
        model=Settings.EMBEDDING_MODEL
    )