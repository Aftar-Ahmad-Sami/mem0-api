from pydantic import BaseModel
from typing import List, Optional

class MemoryItem(BaseModel):
    id: str
    memory: str
    hash: str
    metadata: Optional[dict]
    created_at: str
    updated_at: Optional[str]
    user_id: str

class RelationItem(BaseModel):
    source: str
    relationship: str
    target: str

class QueryResponse(BaseModel):
    results: List[MemoryItem]
    relations: List[RelationItem]
