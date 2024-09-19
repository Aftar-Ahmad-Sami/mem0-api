from fastapi import FastAPI
"""
This module initializes and configures the FastAPI application.

It includes:
- Importing necessary modules and routers.
- Creating an instance of the FastAPI application.
- Including the API router with a specified prefix.
- Defining a root endpoint that returns a welcome message.

Attributes:
    app (FastAPI): The FastAPI application instance.

Routes:
    GET /: Returns a welcome message.
"""
from app.api.routes import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application"}
