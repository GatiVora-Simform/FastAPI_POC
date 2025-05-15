from fastapi import FastAPI
from contextlib import asynccontextmanager

from router import auth_router, todo_router, user_router
from utils.init_db import create_tables

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tables()
    print("Database tables created.")
    yield
    print("Application is shutting down.")


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(todo_router.router)