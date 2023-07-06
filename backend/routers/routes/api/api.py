from fastapi import APIRouter

from routers.routes.api.v1 import v1


def create_api_router() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(v1.router, prefix="/v1", tags=["v1"])
    return api_router


router = create_api_router()