from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from repository.user_repository import UserRepository
from schemas.user_schema import UserInput, UserOutput

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create(self, userin: UserInput) -> UserOutput:
        if self.repository.get_by_email(userin.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists with this email",
            )
        if self.repository.get_by_username(userin.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists with this username",
            )
        user = self.repository.create(userin)
        return UserOutput.model_validate(user)

    def get_all(self) -> list[UserOutput]:
        users = self.repository.get_all_users()
        return [UserOutput.model_validate(user) for user in users]

    def get_by_email(self, email: str) -> UserOutput:
        user = self.repository.get_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        return UserOutput.model_validate(user)
    
    def get_by_username(self, username: str) -> UserOutput:
        user = self.repository.get_by_username(username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        return UserOutput.model_validate(user)

    def get_by_id(self, user_id: UUID) -> UserOutput:
        user = self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        return UserOutput.model_validate(user)

    def update_user(self, user_id: UUID, userin: UserInput) -> UserOutput:
        user = self.repository.update_user(user_id, userin)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        return UserOutput.model_validate(user)

    def delete_user(self, user_id: UUID) -> UserOutput:
        user = self.repository.delete_user(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        return UserOutput.model_validate(user)
