from app.core.config import Config
"""
This module initializes and configures the Memory object using settings from the Config class.

Classes:
    None

Functions:
    None

Variables:
    config (dict): Configuration dictionary for the Memory object, including settings for LLM, vector store, and graph store.
    memory (Memory): An instance of the Memory class initialized with the provided configuration.

Configuration Details:
    - LLM (Language Model):
        - provider: The provider of the language model (e.g., "openai").
        - config: Configuration settings for the language model, including model type and temperature.
    - Vector Store:
        - provider: The provider of the vector store (e.g., "qdrant").
        - config: Configuration settings for the vector store, including collection name, URL, and API key.
    - Graph Store:
        - provider: The provider of the graph store (e.g., "neo4j").
        - config: Configuration settings for the graph store, including URL, username, and password.
    - version: The version of the configuration.

Usage:
    This module is intended to be imported and used within the application to manage memory-related operations.
"""
from mem0 import Memory

config = {
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4o",
            "temperature": 0.2,
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": Config.QDRANT_COLLECTION,
            "url": Config.QDRANT_URL,
            "api_key": Config.QDRANT_API_KEY
        }
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": Config.NEO4J_URL,
            "username": Config.NEO4J_USERNAME,
            "password": Config.NEO4J_PASSWORD
        },
    },
    "version": "v1.1"
}

memory = Memory.from_config(config_dict=config)
