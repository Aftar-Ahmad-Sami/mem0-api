import asyncio
from fastapi import APIRouter, HTTPException
from app.models.request_models import QueryRequest
from app.models.response_models import QueryResponse
from app.models.user_models import UserRequest
from app.core.memory_manager import memory
import logging
from fastapi import APIRouter, HTTPException
from app.models.response_models import QueryResponse, MemoryItem, RelationItem
from app.core.memory_manager import memory
import concurrent.futures

# Initialize the router and logger
router = APIRouter()
logger = logging.getLogger(__name__)

def add_memory_blocking(text: str, user_id: str):
    memory.add(text, user_id=user_id)

def search_memory_blocking(query: str, user_id: str):
    return memory.search(query, user_id=user_id)

def delete_all_memory_blocking(user_id: str):
    memory.delete_all(user_id=user_id)

def fetch_all_memory_blocking(user_id: str):
    return memory.get_all(user_id=user_id)

@router.post("/add", response_model=dict)
async def add_memory(request: QueryRequest):
    try:
        await memory.add(request.text, user_id=request.user_id)
        return {"message": "Text added successfully"}
    except Exception as e:
        logger.error(f"Error in /add endpoint: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/search", response_model=QueryResponse)
async def search_memory(request: QueryRequest):
    try: 
        with concurrent.futures.ThreadPoolExecutor() as executor:  
            loop = asyncio.get_event_loop()    
            results = await loop.run_in_executor(executor, search_memory_blocking,request.query, request.user_id)
        return QueryResponse(
            results=[MemoryItem(**item) for item in results.get('results', [])],
            relations=[RelationItem(**relation) for relation in results.get('relations', [])]
        )
    except Exception as e:
        logger.error(f"Error in /search endpoint: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/get_all", response_model=QueryResponse)
async def get_all_memory(request: UserRequest):
    try:
        user_id = request.user_id

        # Run blocking code in a separate thread
        with concurrent.futures.ThreadPoolExecutor() as executor:
            loop = asyncio.get_event_loop()
            results = await loop.run_in_executor(executor, fetch_all_memory_blocking, user_id)

        # Ensure results is in the format expected by QueryResponse
        return QueryResponse(
            results=[MemoryItem(**item) for item in results.get('results', [])],
            relations=[RelationItem(**relation) for relation in results.get('relations', [])]
        )
    except Exception as e:
        logger.error(f"Error in /get_all endpoint: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/delete_all", response_model=dict)
async def delete_all_memory(user_id: str):
    try:
        await memory.delete_all(user_id=user_id)
        return {"message": "All texts deleted successfully"}
    except Exception as e:
        logger.error(f"Error in /delete_all endpoint: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
