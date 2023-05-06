from fastapi import FastAPI
from app.api.todos.router import todos_router

app = FastAPI()
app.include_router(todos_router, prefix="/api")
