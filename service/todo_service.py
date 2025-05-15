from sqlalchemy.orm import Session
from models.user_models import User
from repository.todo_repository import TodoRepository
from schemas.todo_schema import TodoInput


class TodoService:
    def __init__(self, db: Session):
        self.repo = TodoRepository(db)

    def create_todo(self, todo_in: TodoInput, user: User):
        return self.repo.create(todo_in, user)

    def get_all_todos(self, user: User):
        return self.repo.get_all_by_user(user)

    def get_todo_by_id(self, todo_id: int, user: User):
        return self.repo.get_by_id(todo_id, user)

    def update_todo(self, todo_id: int, todo_in: TodoInput, user: User):
        return self.repo.update(todo_id, todo_in, user)

    def delete_todo(self, todo_id: int, user: User):
        return self.repo.delete(todo_id, user)
