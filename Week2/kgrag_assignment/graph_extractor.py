from langchain_core.prompts import ChatPromptTemplate

from graph_models import KnowledgeGraph
from llm_factory import get_llm

class GraphExtractor:
    def __init__(self):
        self.llm = get_llm().with_structured_output(KnowledgeGraph)

        self.prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
        You are building a Knowledge Graph.

Use ONLY the following node types:

- Scheme
- Department
- Beneficiary
- Benefit

Use ONLY the following relationship types:

Department -> Scheme
MANAGES

Scheme -> Beneficiary
AVAILABLE_TO

Scheme -> Benefit
OFFERS

Do not invent new node types.

Do not invent new relationship types.

Return ONLY a valid KnowledgeGraph object.
        """
                ),
                (
                    "human",
                    """
        {document}
        """
                )
            ]
        )

        self.chain = (
            self.prompt | self.llm
        )

    def extract(self, document:str) -> KnowledgeGraph:
        return self.chain.invoke({"document":document})