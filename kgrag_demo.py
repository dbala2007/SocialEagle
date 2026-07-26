from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
import sys
import certifi

if sys.platform == "win32":
    os.environ.setdefault("SSL_CERT_FILE", certifi.where())

load_dotenv()

loader = TextLoader("sample.txt")
raw_documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

documents = text_splitter.split_documents(raw_documents)

print(f"Total chunks created: {len(documents)}\n")
for i, doc in enumerate(documents):
    print(f"---- Chunk {i+1} ----")
    print(doc.page_content)

print("Initializing LLM and Graph Transformer")

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

transformer = LLMGraphTransformer(llm=llm)

print("Extracting graph data from text chunks")
graph_documents = transformer.convert_to_graph_documents(documents)

print(f"Extracted {len(graph_documents)} graph document structures")
for i, graph_doc in enumerate(graph_documents):
    print(f"=== Graph Data from chunk {i+1} ===")
    print("Nodes (Entities) ")
    for node in graph_doc.nodes:
        print(f" - ID: {node.id}, Type: {node.type}")

    print("Edges (Relationships) ")
    for rel in graph_doc.relationships:
        print(f" - {rel.source.id} --[{rel.type}]--> {rel.target.id}")
    print()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE")

graph = GraphDatabase.driver(NEO4J_URI,
    auth=(NEO4J_USERNAME,NEO4J_PASSWORD)
)

try:
    graph.verify_connectivity()
    print("\nConnected to Neo4j")
except Exception as e:
    print(f"Connection error {e}")
    graph.close()
    exit()

with graph.session() as session:

    for graph_doc in graph_documents:

        # Insert nodes
        for node in graph_doc.nodes:

            session.run(
                """
                MERGE (n:Entity {id:$id})
                SET n.type=$type
                """,
                id=node.id,
                type=node.type
            )

        # Insert relationships
        for rel in graph_doc.relationships:

            relationship = rel.type.replace(" ", "_").upper()

            query = f"""
            MATCH (a:Entity {{id:$source}})
            MATCH (b:Entity {{id:$target}})
            MERGE (a)-[r:`{relationship}`]->(b)
            """

            session.run(
                query,
                source=rel.source.id,
                target=rel.target.id
            )

    print("Graph imported successfully.")

    result = session.run("""
        MATCH (n)
        RETURN n
    """)

    for record in result:
        print(record["n"])

graph.close()


print("\nDone.")
