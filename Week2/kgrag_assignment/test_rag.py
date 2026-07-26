from rag_chain import RAGChain

def main():
    rag = RAGChain()

    response = rag.invoke(
        "Which schemes are available for women farmers?"
    )

    print(response.answer)

    for doc in response.sources:
        print(f"Scheme : {doc.scheme_name}")
        print(f"URL    : {doc.url}")
        print()

if __name__ == "__main__":
    main()