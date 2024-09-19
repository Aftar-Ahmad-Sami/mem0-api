import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    NEO4J_URL = os.getenv('NEO4J_URL')
    NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
    QDRANT_COLLECTION = os.getenv('QDRANT_COLLECTION')
    QDRANT_URL = os.getenv('QDRANT_URL')
    QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')
    USER_ID = os.getenv('USER_ID')
