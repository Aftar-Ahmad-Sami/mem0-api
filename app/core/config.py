import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Configuration class for environment variables.

    Attributes:
        NEO4J_URL (str): URL for the Neo4j database.
        NEO4J_USERNAME (str): Username for the Neo4j database.
        NEO4J_PASSWORD (str): Password for the Neo4j database.
        QDRANT_COLLECTION (str): Name of the Qdrant collection.
        QDRANT_URL (str): URL for the Qdrant service.
        QDRANT_API_KEY (str): API key for the Qdrant service.
        USER_ID (str): User ID for the application.
    """
    NEO4J_URL = os.getenv('NEO4J_URL')
    NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
    QDRANT_COLLECTION = os.getenv('QDRANT_COLLECTION')
    QDRANT_URL = os.getenv('QDRANT_URL')
    QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')
    USER_ID = os.getenv('USER_ID')
    X_API_KEY = os.getenv('X_API_KEY')
