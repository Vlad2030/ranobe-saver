from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from core.database import Base


class UsersDatabase(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(length=12))
    username = Column(String())
    full_name = Column(String())
    created_at = Column(DateTime, default=datetime.now)
