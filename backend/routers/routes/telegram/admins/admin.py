from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from core.crud.admins import Admins as CRUDAdmins
from core.database import AsyncSession, get_async_session
from schemas.responses.admins import Admin, Admins, AdminById, AdminCreated

router = APIRouter(tags=["admins"])

@router.get(
    path="/",
    response_model=Admins,
)
async def get_admins(
        session: AsyncSession = Depends(get_async_session),
) -> JSONResponse:
    admins = CRUDAdmins(session)
    admin_list = await admins.get_all()
    return {
        "count": len(admin_list),
        "admins": admin_list,
    }

@router.get(
    path="/{user_id}/",
    response_model=AdminById
)
async def get_admin_by_user_id(
        user_id: str,
        session: AsyncSession = Depends(get_async_session),
) -> JSONResponse:
    admins = CRUDAdmins(session)
    admin = await admins.get_one_by_id(user_id)
    exist = await admins.is_exist(admin.username)
    return {
        "admin": admin,
        "exist": exist,
    }

@router.post(
    path="/",
    response_model=AdminCreated,
)
async def add_admin(
        admin: Admin,
        session: AsyncSession = Depends(get_async_session)
) -> JSONResponse:
    admins = CRUDAdmins(session)
    if await admins.get_one_by_id(admin.user_id):
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="admin exist",
        )
    new_admin = await admins.create(admin)
    return {
        "admin": new_admin,
        "created": True,
    }

@router.delete(
    path="/",
)
async def delete_admin(
        user_id: str,
        session: AsyncSession = Depends(get_async_session)
) -> JSONResponse:
    admins = CRUDAdmins(session)
    admin = await admins.get_one_by_id(user_id)
    if not admin:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="admin doesn't exist",
        )
    await admins.delete_by_id(user_id)
    return {
        "admin": admin,
        "deleted": True,
    }
