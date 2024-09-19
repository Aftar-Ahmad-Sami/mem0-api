from pydantic import BaseModel
from typing import List, Optional, Dict

class MemoryItem(BaseModel):
    """
    MemoryItem is a Pydantic model representing a memory item.

    Attributes:
        id (str): Unique identifier for the memory item.
        memory (str): The memory content.
        hash (str): Hash value of the memory content.
        metadata (Optional[dict]): Additional metadata associated with the memory item.
        created_at (str): Timestamp when the memory item was created.
        updated_at (Optional[str]): Timestamp when the memory item was last updated.
        user_id (str): Identifier of the user who owns the memory item.
    """
    id: str
    memory: str
    hash: str
    metadata: Optional[dict]
    created_at: str
    updated_at: Optional[str]
    user_id: str

class AddMemoryItem(BaseModel):
    """
    AddMemoryItem is a Pydantic model representing the structure of a memory item to be added.

    Attributes:
        memory (str): The memory content.
        event (str): The event associated with the memory.
        previous_memory (Optional[str]): The previous memory content, if any.
    """
    memory: str
    event: str
    previous_memory: Optional[str]

class RelationItem(BaseModel):
    """
    RelationItem represents a model for defining a relationship between two entities.

    Attributes:
        source (str): The source entity in the relationship.
        relationship (str): The type of relationship between the source and target entities.
        target (str): The target entity in the relationship.
    """
    source: str
    relationship: str
    target: str

class QueryResponse(BaseModel):
    """
    QueryResponse is a Pydantic model representing the response structure for a query.

    Attributes:
        results (List[MemoryItem]): A list of memory items returned by the query.
        relations (List[RelationItem]): A list of relation items associated with the query results.
    """
    results: List[MemoryItem]
    relations: List[RelationItem]

class AddQueryResponse(BaseModel):
    """
    AddQueryResponse is a Pydantic model that represents the response structure for adding a query.

    Attributes:
        results (List[AddMemoryItem]): A list of AddMemoryItem objects representing the results of the query.
        relations (List[RelationItem]): A list of RelationItem objects representing the relations associated with the query.
    """
    results: List[AddMemoryItem]
    relations: List[RelationItem]
