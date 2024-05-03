from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import get_user, is_user_locked
from app.core.database import get_async_session
from app.crud.user import user_crud
from app.schemas.user import UserCreate, UserDB

router = APIRouter()


@router.post("/user_create", response_model=UserDB, response_model_exclude_none=True)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_async_session)):
    new_user = await user_crud.create(user, session)
    return new_user


@router.get("/all_users", response_model=list[UserDB])
async def get_users(session: AsyncSession = Depends(get_async_session)):
    users = await user_crud.get_multi(session)
    return users


@router.post("/lock_user", response_model=UserDB)
async def acquire_lock(user_id: UUID, session: AsyncSession = Depends(get_async_session)):
    user = await get_user(user_id, session)
    is_user_locked(user, True)
    await user_crud.set_lock(user, session, True)
    return user


@router.post("/unlock_user", response_model=UserDB)
async def release_lock(user_id: UUID, session: AsyncSession = Depends(get_async_session)):
    user = await get_user(user_id, session)
    is_user_locked(user, False)
    await user_crud.set_lock(user, session, False)
    return user
