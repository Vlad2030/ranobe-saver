# from core.database import Base, engine
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from starlette import status

from core.database import Base, engine
from config import app
from routers.router import router

application = FastAPI(
    debug=app.BACKEND_DEBUG,
    title=app.BACKEND_TITLE,
    description=app.BACKEND_DESCRIPTION,
    version=app.BACKEND_VERSION,
    openapi_url=app.BACKEND_OPENAPI_URL,
    docs_url=app.BACKEND_DOCS_URL,
    redoc_url=app.BACKEND_REDOC_URL,
    swagger_ui_oauth2_redirect_url=app.BACKEND_SWAGGER_UI_OAUTH2_REDIRECT_URL,
    terms_of_service=app.BACKEND_TERMS_OF_SERVICE,
    contact=app.BACKEND_CONTACT,
    license_info=app.BACKEND_LICENSE_INFO,
    openapi_prefix=app.BACKEND_OPENAPI_PREFIX,
)
application.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=app.BACKEND_ALLOW_ORIGINS,
    allow_origin_regex=app.BACKEND_ALLOW_ORIGIN_REGEX,
    allow_methods=app.BACKEND_ALLOW_METHODS,
    allow_headers=app.BACKEND_ALLOW_HEADERS,
    allow_credentials=app.BACKEND_ALLOW_CREDENTIALS,
    expose_headers=app.BACKEND_EXPOSE_HEADERS,
    max_age=app.BACKEND_MAX_AGE,
    )



application.include_router(router=router)

@application.on_event("startup")
async def startup() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return logger.info("Application startup")

@application.on_event("shutdown")
async def shutdown() -> None:
    return logger.warning("Application shutdown")
