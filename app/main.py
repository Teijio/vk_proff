import uvicorn


from fastapi import FastAPI


class Boo:
    pass


# from fastapi.middleware.cors import CORSMiddleware

# from app.api.httpx_client import on_shutdown, on_start_up
# from app.api.routers import main_router
# from app.core.config import settings

app = FastAPI()

# origins = ["*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
# app.include_router(main_router)
