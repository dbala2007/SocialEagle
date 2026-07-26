from neo4j import GraphDatabase

from settings import Settings


class Neo4jRetriever:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            Settings.NEO4J_URI,
            auth=(
                Settings.NEO4J_USERNAME,
                Settings.NEO4J_PASSWORD
            )
        )

    def execute(self, cypher: str, parameters: dict | None = None):

        if parameters is None:
            parameters = {}

        with self.driver.session() as session:

            result = session.run(
                cypher,
                parameters
            )

            return [record.data() for record in result]

    def format_results(self, results):

        if not results:
            return "No graph information found."

        lines = []

        for row in results:

            values = []

            for key, value in row.items():
                values.append(f"{key}: {value}")

            lines.append(", ".join(values))

        return "\n".join(lines)

    def close(self):
        self.driver.close()