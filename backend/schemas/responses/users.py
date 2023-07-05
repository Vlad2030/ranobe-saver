from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    user_id: str = "112233445"
    username: str = "user"
    full_name: str = "User"
    created_at: datetime


class UserCreated(BaseModel):
    admin: User
    created: bool = True


class UserDeleted(BaseModel):
    admin: User
    deleted: bool = True


class UserById(BaseModel):
    admin: User
    is_exist: bool = True


class Users(BaseModel):
    count: int
    admins: list[User]
