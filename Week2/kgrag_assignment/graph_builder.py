import json

from settings import Settings
from graph_extractor import GraphExtractor
from cypher_generator import CypherGenerator
from neo4j_writer import Neo4jWriter
from load_document import load_scheme_documents

class GraphBuilder:

    def __init__(self):
        self.extractor = GraphExtractor()
        self.generator = CypherGenerator()
        self.writer = Neo4jWriter(
            uri=Settings.NEO4J_URI,
            username=Settings.NEO4J_USERNAME,
            password=Settings.NEO4J_PASSWORD,
        )

    def build(self):

        documents = load_scheme_documents(Settings.DATA_PATH)

        print(f"Found {len(documents)} Schemes")

        for index, document in enumerate(documents, start=1):

            try:
                print(f"Processing {index}/{len(documents)}")

                text = f"""
        Scheme Title/Name: {document.metadata['scheme_name']}

        {document.page_content}
        """

                graph = self.extractor.extract(text)

                nodes, relationships = self.generator.generate(graph)

                self.writer.write(nodes, relationships)

            except Exception as e:
                print(f"❌ Failed processing scheme {index}: {e}")

if __name__ == "__main__":

    builder = GraphBuilder()
    builder.build()

    print("Graph build completed.")