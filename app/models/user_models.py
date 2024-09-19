from pydantic import BaseModel
class UserRequest(BaseModel):
    """
    UserRequest model for handling user-related requests.

    Attributes:
        user_id (str): A unique identifier for the user.
    """
    user_id: str