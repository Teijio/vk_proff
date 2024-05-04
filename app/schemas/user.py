from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, StringConstraints
from typing_extensions import Annotated

PASSWORD_MIN_LENGTH = 10


class EnvTypes(str, Enum):
    prod = "prod"
    preprod = "preprod"
    stage = "stage"


class DomainTypes(str, Enum):
    canary = "canary"
    regular = "regular"


class UserBase(BaseModel):
    login: EmailStr
    password: Annotated[str, StringConstraints(min_length=PASSWORD_MIN_LENGTH)]
    project_id: UUID
    env: EnvTypes
    domain: DomainTypes


class UserCreate(UserBase):
    pass


class UserDB(UserBase):
    id: UUID
    created_at: datetime
    locktime: Optional[datetime]

    class Config:
        from_attributes = True
        json_encoders = {datetime: lambda dt: dt.strftime("%Y-%m-%d %H:%M:%S")}
