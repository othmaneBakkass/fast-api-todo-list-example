from enum import Enum
from typing import Optional
from fastapi import FastAPI
from sqlmodel import Field, SQLModel, create_engine, Session, select
from pydantic import BaseModel


# database
class TodosTypes(str, Enum):
    personal = "personal"
    business = "business"


class Todos(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    type: TodosTypes = Field(default=TodosTypes.business)


mysql_url = "mysql+pymysql://root:root@127.0.0.1:3306/fastApi_todos_example"
engine = create_engine(mysql_url, echo=True)


# api
class TodoItem(BaseModel):
    content: str
    type: TodosTypes


def create_one_todo(todoItem: TodoItem):
    todo = Todos(content=todoItem.content, type=todoItem.type)

    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.close()


def get_all_todos():
    with Session(engine) as session:
        res = session.exec(select(Todos.id, Todos.type)).all()
        print({"response": res})


app = FastAPI()


@app.post("/todos")
def create_one_todo_controller(todoItem: TodoItem):
    print("🚀 ~ create_one_todo_handler:")
    create_one_todo(todoItem)
    return {"todo": "created"}


@app.get("/todos")
def get_all_todos_controller():
    print("🚀 ~ get_all_todos_controller:")
    get_all_todos()
    return {"todos": "list"}
