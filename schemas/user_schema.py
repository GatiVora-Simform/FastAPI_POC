from datetime import datetime

from pydantic import BaseModel, Field
from config.database import Base
from uuid import UUID

class UserInput(BaseModel):
    email:str
    hashed_password:str
    first_name:str 
    last_name:str | None = None 
    is_admin:bool

class UserIndb(UserInput):
    id:UUID
    created_at: datetime
    updated_at:datetime
    
    class Config:
        orm_mode = True

class UserOutput(UserIndb):
    hashed_password: str = Field(exclude=True)
    class Config:
        orm_mode = True
        from_attributes = True

class UserLogin(BaseModel):
    email:str
    hashed_password:str