import uuid
from sqlalchemy import Boolean, Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config.database import Base

from models.todo_models import TodoModel

# UserBase = declarative_base()

class User(Base):
    __tablename__ = 'users'
    __allowed_unmapped__ = True

    id = Column(UUID(as_uuid = True),primary_key = True,default=uuid.uuid4)
    email = Column(String(length=100), nullable=False, unique=True)
    username = Column(String(length=50), nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String(length=50),nullable=False)
    last_name = Column(String(length=50))
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(),onupdate=func.now())

    todos = relationship(TodoModel, back_populates="user", cascade="all, delete")