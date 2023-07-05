from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    create_async_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.database import (DATABASE_DB, DATABASE_HOST, DATABASE_PASSWORD,
                         DATABASE_PORT, DATABASE_USER)

DATABASE_URL = (f"postgresql+asyncpg://"
                f"{DATABASE_USER}:{DATABASE_PASSWORD}"
                f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}")
Base = declarative_base()
metadata = MetaData()
engine = create_async_engine(url=DATABASE_URL, echo=False)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

def create_all(engine: AsyncEngine) -> None:
    return metadata.create_all(engine)

async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session