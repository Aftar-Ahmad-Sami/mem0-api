from pydantic import BaseModel

class QueryRequest(BaseModel):
    """
    QueryRequest is a Pydantic model representing a query request.

    Attributes:
        query (str): The query string.
        user_id (str): The ID of the user making the request.
    """
    query: str
    user_id: str
