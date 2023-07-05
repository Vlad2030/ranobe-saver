import time

from fastapi import APIRouter, HTTPException, responses, status

from config.app import BACKEND_API_VERSION
from routers.routes.api.v1.ranobes import ranobe
from schemas.responses.health_check import HealthCheck
from schemas.responses.server_time import ServerTime


def create_api_router() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(ranobe.router, prefix="/ranobes", tags=["ranobes"])
    @api_router.get(
        path="/",
        description="Work status check",
        response_model=HealthCheck,
        status_code=status.HTTP_200_OK,
    )
    async def work_status() -> responses.JSONResponse:
        match BACKEND_API_VERSION:
            case "v1":
                return {
                    "work_status": True,
                }
            case _:
                return {
                    "work_status": False,
                }

    @api_router.get(
        path="/time",
        description="Get server time",
        response_model=ServerTime,
        status_code=status.HTTP_200_OK,
    )
    async def server_time() -> responses.JSONResponse:
        return {
            "server_time": int(time.time() * 1000),
        }

    return api_router


router = create_api_router()