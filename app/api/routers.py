from fastapi import APIRouter

from app.api.endpoints import user_router

main_router = APIRouter(prefix="/users")
main_router.include_router(user_router)
