from pydantic import BaseModel

class NodeOperation(BaseModel):
    label: str
    name: str


class RelationshipOperation(BaseModel):
    source_label: str
    source_name: str

    target_label: str
    target_name: str

    relationship: str