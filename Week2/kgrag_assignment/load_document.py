import json

from langchain_core.documents import Document
from settings import Settings

def load_scheme_documents(json_file: str):
    with open(json_file, "r", encoding='utf-8') as f:
        schemes = json.load(f)

    documents = []

    for scheme in schemes:
        page_content = []
        metadata = {
            "scheme_name": scheme.get("Scheme Title/Name", {}).get("value",""),
            "url": scheme.get("url",""),
            "title": scheme.get("title","")
        }

        page_content.append(
            f"Scheme Title/Name: {metadata['scheme_name']}"
        )

        for key, value in scheme.items():
            if key in ["Scheme Title/Name", "url", "title"]:
                continue

            if not isinstance(value, dict):
                continue

            text = value.get("value","").strip()

            if text == "":
                continue

            page_content.append(f"{key}: {text}")

        document = Document(
            page_content="\n".join(page_content),
            metadata=metadata
        )

        documents.append(document)

    return documents

if __name__ == "__main__":
    docs = load_scheme_documents(Settings.DATA_PATH)
    # print(f"Total documents: {len(docs)}")
    # print(f"Metadata: {docs[0].metadata}")
    # print(f"Content: {docs[0].page_content}")