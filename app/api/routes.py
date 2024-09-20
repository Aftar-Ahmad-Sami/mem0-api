import asyncio
from app.core import auth
from fastapi import APIRouter, HTTPException
from app.models.request_models import QueryRequest
from app.models.response_models import AddQueryResponse, QueryResponse
from app.models.user_models import UserRequest
from app.core.memory_manager import memory
import logging
from fastapi import APIRouter, HTTPException, Depends
from app.models.response_models import QueryResponse, MemoryItem, AddMemoryItem, RelationItem
from app.core.memory_manager import memory
import concurrent.futures

# Initialize the router and logger
router = APIRouter(dependencies=[Depends(auth.validate_api_key)])
logger = logging.getLogger(__name__)

def add_memory_blocking(query: str, user_id: str):
    """
    Blocking function to add memory.

    Args:
        query (str): The query string to add to memory.
        user_id (str): The user ID associated with the query.

    Returns:
        dict: The result of the memory addition.
    """
    return memory.add(query, user_id=user_id)

def search_memory_blocking(query: str, user_id: str):
    """
    Blocking function to search memory.

    Args:
        query (str): The query string to search in memory.
        user_id (str): The user ID associated with the query.

    Returns:
        dict: The search results from memory.
    """
    return memory.search(query, user_id=user_id)

def delete_all_memory_blocking(user_id: str):
    """
    Blocking function to delete all memory for a user.

    Args:
        user_id (str): The user ID whose memory will be deleted.

    Returns:
        None
    """
    return memory.delete_all(user_id=user_id)

def fetch_all_memory_blocking(user_id: str):
    """
    Blocking function to fetch all memory for a user.

    Args:
        user_id (str): The user ID whose memory will be fetched.

    Returns:
        dict: All memory items for the user.
    """
    return memory.get_all(user_id=user_id)

@router.post("/add", response_model=AddQueryResponse)
async def add_memory(request: QueryRequest):
    """
    Endpoint to add a query to memory.

    Args:
        request (QueryRequest): The request body containing the query and user ID.

    Returns:
        AddQueryResponse: The response containing added memory items and relations.
    """
    try:
        # Use ThreadPoolExecutor to run blocking code in a separate thread
        with concurrent.futures.ThreadPoolExecutor() as executor:
            loop = asyncio.get_event_loop()
            results = await loop.run_in_executor(executor, add_memory_blocking, request.query, request.user_id)
        
        # Convert results to response model
        return AddQueryResponse(
            results=[AddMemoryItem(**item) for item in results.get('results', [])],
            relations=[RelationItem(**relation) for relation in results.get('relations', [])]
        )
    except Exception as e:
        logger.error(f"Error in /add endpoint: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/search", response_model=QueryResponse)
async def search_memory(request: QueryRequest):
    """
    Endpoint to search memory.

    Args:
        request (QueryRequest): The request body containing the query and user ID.

    Returns:
        QueryResponse: The response containing search results and relations.
    """
    try:
        # Use ThreadPoolExecutor to run blocking code in a separate thread
        with concurrent.futures.ThreadPoolExecutor() as executor:
            loop = asyncio.get_event_loop()
            results = await loop.run_in_executor(executor, search_memory_blocking, request.query, request.user_id)
        
        # Convert results to response model
        return QueryResponse(
            results=[MemoryItem(**item) for item in results.get('results', [])],
            relations=[RelationItem(**relation) for relation in results.get('relations', [])]
        )
    except Exception as e:
        logger.error(f"Error in /search endpoint: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/get_all", response_model=QueryResponse)
async def get_all_memory(request: UserRequest):
    """
    Endpoint to fetch all memory for a user.

    Args:
        request (UserRequest): The request body containing the user ID.

    Returns:
        QueryResponse: The response containing all memory items and relations.
    """
    try:
        user_id = request.user_id

        # Use ThreadPoolExecutor to run blocking code in a separate thread
        with concurrent.futures.ThreadPoolExecutor() as executor:
            loop = asyncio.get_event_loop()
            results = await loop.run_in_executor(executor, fetch_all_memory_blocking, user_id)

        # Convert results to response model
        return QueryResponse(
            results=[MemoryItem(**item) for item in results.get('results', [])],
            relations=[RelationItem(**relation) for relation in results.get('relations', [])]
        )
    except Exception as e:
        logger.error(f"Error in /get_all endpoint: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/delete_all", response_model=dict)
async def delete_all_memory(user_id: str):
    """
    Endpoint to delete all memory for a user.

    Args:
        user_id (str): The user ID whose memory will be deleted.

    Returns:
        dict: A message indicating successful deletion.
    """
    try:
        # Use ThreadPoolExecutor to run blocking code in a separate thread
        with concurrent.futures.ThreadPoolExecutor() as executor:
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(executor, delete_all_memory_blocking, user_id)
        
        # Return success message
        return {"message": "All texts deleted successfully"}
    except Exception as e:
        logger.error(f"Error in /delete_all endpoint: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
