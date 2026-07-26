from neo4j import GraphDatabase
from settings import Settings

class Neo4jClient:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            Settings.NEO4J_URI,
            auth=(
                Settings.NEO4J_USERNAME,
                Settings.NEO4J_PASSWORD
            )
        )

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(
                query,
                parameters or {}
            )
            return list(result)