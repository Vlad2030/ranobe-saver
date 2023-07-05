import typing

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.admins import AdminsDatabase
from schemas.responses.admins import Admin


class Admins:
    def __init__(self, session) -> None:
        self.session: AsyncSession = session

    async def create(
            self,
            admin: Admin,
    ) -> typing.Union[Admin, bool]:
        admin = AdminsDatabase(**admin.dict())
        if await self.get_one_by_id(admin.id):
            return False
        self.session.add(admin)
        await self.session.flush()
        await self.session.refresh(admin)
        await self.session.commit()
        return admin

    async def get_all(self) -> typing.List[Admin]:
        query = select(AdminsDatabase)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_one_by_id(self, id: int) -> Admin:
        query = select(AdminsDatabase).where(AdminsDatabase.user_id == id)
        result = await self.session.execute(query)
        return result.scalars()

    async def delete_by_id(self, id: int) -> typing.Union[Admin, bool]:
        query = delete(AdminsDatabase).where(AdminsDatabase.user_id == id)
        result = await self.session.execute(query)
        if result is None:
            return False
        await self.session.flush()
        await self.session.commit()
        return result

    async def is_exist(
        self,
        id: int,
    ) -> typing.Union[Admin, bool]:
        query = select(AdminsDatabase).where(AdminsDatabase.user_id == id)
        result = await self.session.execute(query)
        if len(result.scalars().all()) >= 1:
            return True
        return False