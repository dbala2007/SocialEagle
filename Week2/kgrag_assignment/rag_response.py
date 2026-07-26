from pydantic import BaseModel

class Source(BaseModel):
    scheme_name: str
    url: str

class RAGResponse(BaseModel):
    question: str
    answer: str
    sources: list[Source]