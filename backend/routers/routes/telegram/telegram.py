from fastapi import APIRouter

from routers.routes.telegram.admins import admin
from routers.routes.telegram.users import user


def create_api_router() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(admin.router, prefix="/admins", tags=["admins"])
    api_router.include_router(user.router, prefix="/users", tags=["users"])
    return api_router


router = create_api_router()