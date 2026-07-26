from neo4j_client import Neo4jClient

def main():
    client = Neo4jClient()
    result = client.execute_query(
        """
    MATCH (n)
    RETURN labels(n) AS labels,
           n.name AS name
    """ 
    )

    for record in result:
        print(record)

    client.close()

if __name__ == "__main__":
    main()