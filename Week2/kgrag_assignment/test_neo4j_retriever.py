from neo4j_retriever import Neo4jRetriever

retriever = Neo4jRetriever()

query = """
MATCH (s:SCHEME)
RETURN s.name AS scheme
LIMIT 5
"""

result = retriever.execute(query)

print(result)

retriever.close()