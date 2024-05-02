from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from app.core.database import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    pass 