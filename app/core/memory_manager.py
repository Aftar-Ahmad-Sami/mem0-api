from app.core.config import Config
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
