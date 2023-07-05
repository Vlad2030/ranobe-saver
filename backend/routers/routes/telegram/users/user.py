from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from core.crud.users import Users as CRUDUsers
from core.database import AsyncSession, get_async_session
from schemas.responses.users import User, UserCreated, UserDeleted, UserById, Users

router = APIRouter(tags=["users"])

@router.get(
    path="/",
    response_model=Users,
)
async def get_users(
        session: AsyncSession = Depends(get_async_session),
) -> JSONResponse:
    users = CRUDUsers(session)
    user_list = await users.get_all()
    return {
        "count": len(user_list),
        "users": user_list,
    }

@router.get(
    path="/{user_id}/",
    response_model=UserById
)
async def get_user_by_user_id(
        user_id: str,
        session: AsyncSession = Depends(get_async_session),
) -> JSONResponse:
    users = CRUDUsers(session)
    user = await users.get_one_by_id(user_id)
    exist = await users.is_exist(user.username)
    return {
        "user": user,
        "exist": exist,
    }

@router.post(
    path="/",
    response_model=UserCreated,
)
async def add_user(
        user: User,
        session: AsyncSession = Depends(get_async_session)
) -> JSONResponse:
    users = CRUDUsers(session)
    if await users.get_one_by_id(user.user_id):
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user exist",
        )
    new_user = await users.create(user)
    return {
        "user": new_user,
        "created": True,
    }

@router.delete(
    path="/",
)
async def delete_user(
        user_id: str,
        session: AsyncSession = Depends(get_async_session)
) -> JSONResponse:
    users = CRUDUsers(session)
    user = await users.get_one_by_id(user_id)
    if not user:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user doesn't exist",
        )
    await users.delete_by_id(user_id)
    return {
        "user": user,
        "deleted": True,
    }
