from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.user import User


class CRUDUser(CRUDBase):
    async def set_lock(self, user: User, session: AsyncSession, lock: bool):
        user.locktime = datetime.now() if lock else None
        await session.commit()
        await session.refresh(user)
        return user

    async def is_unique_user_login(self, login: str, session: AsyncSession) -> bool:
        result = await session.execute(select(User).where(User.login == login))
        existing_user_login = result.fetchone()
        return not existing_user_login


user_crud = CRUDUser(User)
