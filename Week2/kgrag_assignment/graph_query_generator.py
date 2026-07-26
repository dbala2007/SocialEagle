from langchain_core.prompts import ChatPromptTemplate

from graph_query import GraphQuery
from llm_factory import get_llm


class GraphQueryGenerator:

    def __init__(self):

        self.llm = get_llm().with_structured_output(GraphQuery)

        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are an expert at converting user questions into graph queries.

Ontology

Nodes
- SCHEME
- BENEFICIARY
- BENEFIT
- DEPARTMENT

Relationships

Department -> MANAGES -> Scheme

Scheme -> AVAILABLE_TO -> Beneficiary

Scheme -> OFFERS -> Benefit

Return only the GraphQuery object.
"""
                ),
                ("human", "{question}")
            ]
        )

        self.chain = self.prompt | self.llm

    def generate(self, question: str):

        return self.chain.invoke(
            {
                "question": question
            }
        )