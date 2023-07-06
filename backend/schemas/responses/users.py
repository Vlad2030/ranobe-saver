from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    user_id: str = "112233445"
    username: str = "user"
    full_name: str = "User"
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreated(BaseModel):
    admin: User
    created: bool = True

    class Config:
        orm_mode = True


class UserDeleted(BaseModel):
    admin: User
    deleted: bool = True

    class Config:
        orm_mode = True


class UserById(BaseModel):
    admin: User
    is_exist: bool = True

    class Config:
        orm_mode = True


class Users(BaseModel):
    count: int
    admins: list[User]

    class Config:
        orm_mode = True
