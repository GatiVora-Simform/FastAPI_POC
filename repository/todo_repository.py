from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from models.todo_models import TodoModel
from schemas.todo_schema import TodoInput,TodoOutput
from models.user_models import User

class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, todo_in: TodoInput, current_user: User):
        todo = TodoModel(
            title=todo_in.title,
            description=todo_in.description,
            status=todo_in.status,
            due_date=todo_in.due_date,
            user_id=current_user.id
        )
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def get_all_by_user(self, user: User):
        return self.db.query(TodoModel).filter(TodoModel.user_id == user.id).all()

    def get_by_id(self, todo_id: int, user: User):
        return self.db.query(TodoModel).filter(TodoModel.id == todo_id, TodoModel.user_id == user.id).first()

    def update(self, todo_id: int, todo_in: TodoInput, user: User):
        todo = self.get_by_id(todo_id, user)
        if not todo:
            return None
        for key, value in todo_in.model_dump(exclude_unset=True).items():
            setattr(todo, key, value)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def delete(self, todo_id: int, user: User):
        todo = self.get_by_id(todo_id, user)
        if not todo:
            return None
        self.db.delete(todo)
        self.db.commit()
        return todo
