# from datetime import datetime

# from sqlalchemy import Column, DateTime, String, Text
# from sqlalchemy.dialects.postgresql import INET, JSONB

# from app.core.database import Base


# class ActivityLog(Base):
#     ip_address = Column(INET, unique=True, nullable=False, index=True)
#     user_agent = Column(Text, nullable=False)
#     pixel = Column(String(30), nullable=False)
#     fbclid = Column(String(1000), nullable=False)
#     fbc = Column(String(1000), nullable=False)
#     fbp = Column(String(1000), nullable=True)
#     created_at = Column(DateTime, default=datetime.now(), nullable=False)
#     flow = Column(String(255), nullable=False)
#     extra_data = Column(JSONB, nullable=True)


class Users(Base):
    