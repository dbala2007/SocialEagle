from langchain_core.documents import Document
from settings import Settings

from load_vector_store import load_vector_store

class FAISSRetriever:

    def __init__(self):
        self.vector_store = load_vector_store()

        self.retriever = self.vector_store.as_retriever(
            search_type=Settings.SEARCH_TYPE,
            search_kwargs={
                "k": Settings.RETRIEVER_K
            }
        )

    def invoke(
            self, query:str, k: int = 5,
    ) -> list[Document]:
        """
        Perform semantic similarity search.
        """

        return self.retriever.invoke(query)  