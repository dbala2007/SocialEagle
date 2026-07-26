from pydantic import BaseModel
from graph_models import KnowledgeGraph
from graph_operations import NodeOperation, RelationshipOperation
from graph_extractor import GraphExtractor
from neo4j_writer import Neo4jWriter
from settings import Settings

class CypherGenerator:
    def generate(
        self, graph: KnowledgeGraph
    ):
        node_lookup = {}
        node_operations = []

        for node in graph.nodes:
            node_lookup[node.id] = node

            node_operations.append(
                NodeOperation(
                    label=node.type.value,
                    name=node.name,
                )
            )

        relationship_operations = []

        for rel in graph.relationships:
            source_node = node_lookup[rel.source]
            target_node = node_lookup[rel.target]
            relationship_operations.append(
                RelationshipOperation(
                    source_label=source_node.type.value,
                    source_name=source_node.name,
                    target_label=target_node.type.value,
                    target_name=target_node.name,
                    relationship=rel.type.value,
                )
            )

        return (
            node_operations,
            relationship_operations,
        )

document = """
Scheme Name:
Micro Nutrient Spray

Department:
Agriculture

Beneficiaries:
Farmers

Types of Benefits:
Subsidy

Description:
All farmers are eligible.
"""

extractor = GraphExtractor()

graph = extractor.extract(document)

generator = CypherGenerator()

nodes, relationships = generator.generate(graph)

writer = Neo4jWriter(
    uri=Settings.NEO4J_URI,
    username=Settings.NEO4J_USERNAME,
    password=Settings.NEO4J_PASSWORD,
)

writer.write(nodes, relationships)

writer.close()

