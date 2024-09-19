from pydantic import BaseModel
class UserRequest(BaseModel):
    user_id: str