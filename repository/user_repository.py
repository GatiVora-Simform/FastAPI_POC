from models.user_models import User
from schemas.user_schema import UserInput, UserOutput
from utils.security import hash_password


class UserRepository:
    def __init__(self, db):
        self.db = db

    def create(self, userin: UserInput):
        user = User(
            **userin.model_dump(exclude={'hashed_password'}),
            hashed_password=hash_password(userin.hashed_password)  # Map hashed_password correctly
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return UserOutput.model_validate(user) 

    def get_by_email(self, email:str):
        user =  self.db.query(User).filter(User.email == email).first()
        if user:
            return UserOutput.model_validate(user)
        return None

