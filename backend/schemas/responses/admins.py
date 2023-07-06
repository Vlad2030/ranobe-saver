from pydantic import BaseModel
from datetime import datetime


class Admin(BaseModel):
    user_id: str = "112233445"
    username: str = "admin_user"
    full_name: str = "Admin"
    created_at: datetime

    class Config:
        orm_mode = True


class AdminCreated(BaseModel):
    admin: Admin
    created: bool = True

    class Config:
        orm_mode = True


class AdminDeleted(BaseModel):
    admin: Admin
    deleted: bool = True

    class Config:
        orm_mode = True


class AdminById(BaseModel):
    admin: Admin
    is_exist: bool = True

    class Config:
        orm_mode = True


class Admins(BaseModel):
    count: int = 1
    admins: list[Admin]

    class Config:
        orm_mode = True
