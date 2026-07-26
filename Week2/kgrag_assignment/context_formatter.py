from langchain_core.documents import Document


class ContextFormatter:

    @staticmethod
    def format(
        docs: list[Document]
    ) -> str:

        formatted = []

        for doc in docs:

            formatted.append(
                f"""
Scheme Name:
{doc.metadata.get("scheme_name")}

URL:
{doc.metadata.get("url")}

Details:
{doc.page_content}
"""
            )

        return "\n\n-------------------------\n\n".join(formatted)