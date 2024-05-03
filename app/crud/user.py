from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.user import User


class CRUDUser(CRUDBase):
    async def set_lock(self, user: User, session: AsyncSession, lock: bool):
        user.locktime = datetime.now() if lock else None
        await session.commit()
        await session.refresh(user)
        return user


user_crud = CRUDUser(User)
