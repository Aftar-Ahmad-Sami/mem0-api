import os
from openai import AsyncOpenAI

class OpenAIClient:
    """
    OpenAIClient is a client for interacting with the OpenAI API asynchronously.

    Attributes:
        client (AsyncOpenAI): An instance of the AsyncOpenAI client initialized with the API key from environment variables.

    Methods:
        some_method():
            A placeholder method for future implementation.
    """
    def __init__(self):
        self.client = AsyncOpenAI(api_key=os.getenv('OPENAI_API'))

    async def some_method(self):
        pass
