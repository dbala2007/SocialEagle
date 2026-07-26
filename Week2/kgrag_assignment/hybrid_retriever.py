from graph_query_generator import GraphQueryGenerator
from cypher_query_builder import CypherQueryBuilder
from neo4j_retriever import Neo4jRetriever
from faiss_retriever import FAISSRetriever


class HybridRetriever:

    def __init__(self):
        self.vector_retriever = FAISSRetriever()

        self.graph_query_generator = GraphQueryGenerator()

        self.cypher_builder = CypherQueryBuilder()

        self.neo4j_retriever = Neo4jRetriever()

    def invoke(self, question: str):

        # -----------------------------
        # Graph Retrieval
        # -----------------------------

        graph_context = ""

        try:

            graph_query = self.graph_query_generator.generate(question)

            cypher, params = self.cypher_builder.build(graph_query)

            graph_results = self.neo4j_retriever.execute(
                cypher,
                params
            )

            graph_context = self.neo4j_retriever.format_results(
                graph_results
            )

        except Exception as ex:

            print(f"Graph Retrieval Error : {ex}")

            graph_context = ""

        # -----------------------------
        # Vector Retrieval
        # -----------------------------

        documents = self.vector_retriever.invoke(question)

        return {
            "graph_context": graph_context,
            "documents": documents
        }

    def close(self):
        self.neo4j_retriever.close()