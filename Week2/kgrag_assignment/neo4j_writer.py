from neo4j import GraphDatabase
from graph_operations import NodeOperation, RelationshipOperation

class Neo4jWriter:
    def __init__(
            self,
            uri: str,
            username: str,
            password: str
            ):
        self.driver = GraphDatabase.driver(
            uri,
            auth=(username, password)
        )

    def close(self):
        self.driver.close()

    def write(
            self, 
            nodes: list[NodeOperation],
            relationships: list[RelationshipOperation],
    ):
        with self.driver.session() as session:
            for node in nodes:
                session.run(
                    f"""
                    MERGE (n:{node.label} {{name:$name}})
                    """,
                    name=node.name
                )

            for rel in relationships:
                session.run(
                    f"""
                    MATCH (a:{rel.source_label} {{name:$source}})
                    MATCH (b:{rel.target_label} {{name:$target}})
                    MERGE (a)-[:{rel.relationship}]->(b)
                    """,
                    source=rel.source_name,
                    target=rel.target_name,
                )