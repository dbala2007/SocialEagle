from pydantic import BaseModel
from enum import Enum

class NodeType(str, Enum):
    SCHEME = "SCHEME"
    DEPARTMENT = "DEPARTMENT"
    BENEFICIARY = "BENEFICIARY"
    BENEFIT = "BENEFIT"

class RelationshipType(str, Enum):
    MANAGES = "MANAGES"
    AVAILABLE_TO = "AVAILABLE_TO"
    OFFERS = "OFFERS"

class GraphNode(BaseModel):
    id: str
    type: NodeType
    name: str


class GraphRelationship(BaseModel):
    source: str
    target: str
    type: RelationshipType


class KnowledgeGraph(BaseModel):
    nodes: list[GraphNode]
    relationships: list[GraphRelationship]