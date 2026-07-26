from langchain_text_splitters import RecursiveCharacterTextSplitter

from load_document import load_scheme_documents
from settings import Settings

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=Settings.CHUNK_SIZE,
        chunk_overlap=Settings.CHUNK_OVERLAP,
        length_function=len,
        is_separator_regex=False
    )

    chunks = text_splitter.split_documents(documents)

    return chunks

if __name__ == "__main__":
    documents = load_scheme_documents("tn_govt_schemes.json")
    print(f"Original Documents: {len(documents)}")

    chunks = split_documents(documents)
    print(f"Total Chunks: {len(chunks)}")