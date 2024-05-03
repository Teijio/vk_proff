import uuid
from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, DateTime, Enum, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import EmailType, StringEncryptedType

from app.core.config import settings
from app.core.database import Base


class EnvTypes(str, Enum):
    prod = "prod"
    preprod = "CREATED"
    stage = "stage"


class DomainTypes(str, Enum):
    canary = "canary"
    regular = "regular"


class User(Base):
    id = Column(UUID, primary_key=True, unique=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    login = Column(EmailType, nullable=False, unique=True, index=True)
    password = Column(StringEncryptedType(String, settings.secret_key), nullable=False)
    project_id = Column(UUID, nullable=False)
    env = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    locktime = Column(TIMESTAMP)
