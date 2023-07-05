from fastapi import APIRouter

from routers.routes.api import api
from routers.routes.telegram import telegram


def create_api_router() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(api.router, prefix="/api")
    api_router.include_router(telegram.router, prefix="/telegram", tags=["telegram"])
    return api_router


router = create_api_router()