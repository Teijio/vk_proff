from typing import Optional
from uuid import UUID

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_async_session
from app.crud.user import user_crud
from app.models.user import User


async def check_unique_user_login(user_login: str, session: AsyncSession = Depends(get_async_session)) -> bool:
    is_unique_user_login = user_crud.is_unique_user_login(user_login, session)
    if not await is_unique_user_login:
        raise HTTPException(status_code=422, detail="Данный login уже занят")


async def get_user(user_id: UUID, session: AsyncSession = Depends(get_async_session)) -> Optional[User]:
    user = await user_crud.get_by_attribute("id", user_id, session)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


def is_user_locked(user: User, lock: bool):
    if user.locktime and lock:
        raise HTTPException(status_code=422, detail="Пользователь занят")
    if not user.locktime and not lock:
        raise HTTPException(status_code=422, detail="Пользователь уже свободен")
