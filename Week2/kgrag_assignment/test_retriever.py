from faiss_retriever import FAISSRetriever

def main():
    retriever = FAISSRetriever()

    query = "Schemes for women farmers"

    results = retriever.invoke(query)

    print(f"\nQuery: {query}")

    for index, document in enumerate(results, start=1):
        print(f"\nResult: {index}")
        print("Metadata")
        print(document.metadata)
        print()
        print(document.page_content)

if __name__ == "__main__":
    main()