from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from llm_factory import get_llm
from hybrid_retriever import HybridRetriever
from rag_response import Source, RAGResponse
from context_formatter import ContextFormatter
from chat_message import ChatMessage
from history_formatter import HistoryFormatter

class RAGChain:
    def __init__(self):
        self.retriever = HybridRetriever()
        self.llm = get_llm()
        self.prompt = ChatPromptTemplate.from_messages(
[
    (
        "system",
"""
You are an expert assistant for Tamil Nadu Government Schemes.

Answer ONLY using the supplied information.

Graph Information
-----------------
{graph_context}

Document Information
--------------------
{vector_context}

Conversation History
--------------------
{history}

Instructions:

- Use the Graph Information to identify relevant schemes and relationships.
- Use the Document Information to explain the schemes.
- Never invent information.
- If multiple schemes match, list all of them.
- If no answer is available, say so.
"""
    ),
    ("human", "{question}")
]
        )

        self.chain = (
            self.prompt
            | self.llm
            | StrOutputParser()
        )

    def invoke(self, question: str, history: list[ChatMessage] | None = None):
        result = self.retriever.invoke(question)

        graph_context = result["graph_context"]
        docs = result["documents"]

        vector_context = ContextFormatter.format(docs)

        # print("Context sent to LLM")
        # print(context)
        history_text = HistoryFormatter.format(history)

        answer = self.chain.invoke(
            {
                "history":history_text,
                "graph_context": graph_context,
                "vector_context": vector_context,
                "question": question
            }
        )

        sources = [
                    Source(
                        scheme_name=doc.metadata["scheme_name"],
                        url=doc.metadata["url"]
                    )
                    for doc in docs
                ]
        
        return RAGResponse(
            question=question,
            answer=answer,
            sources=sources
        )