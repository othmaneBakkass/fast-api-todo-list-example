from pydantic import BaseModel
from sqlmodel import Session, select
from ...db.models import Todos, TodosTypes
from ...db.engine import engine


class TodoItem(BaseModel):
    content: str
    type: TodosTypes


def create_one_todo(todoItem: TodoItem):
    try:
        todo = Todos(content=todoItem.content, type=todoItem.type)

        with Session(engine) as session:
            session.add(todo)
            session.commit()

            print("🚀 ~ create_one_todo ~ ", todo)
            return (True, {"id": todo.id})
    except:
        print("🚀 ~ create_one_todo ~ error")
        return (False, "database error")


def get_all_todos():
    try:
        with Session(engine) as session:
            res = session.exec(select(Todos)).all()
            session.close()

            print("🚀 ~ get_all_todos ~ ", res)
            return (True, {"todos": res})
    except:
        print("🚀 ~ get_all_todos ~ error")
        return (False, "database error")


def get_todo(id: int):
    try:
        with Session(engine) as session:
            res = session.get(Todos, id)
            print("🚀 ~ get_one_todo ~ ", res)

            return (True, {"todo": res})
    except:
        print("🚀 ~ get_one_todo ~ error")
        return (False, "database error")


class UpdateContentPayload(BaseModel):
    id: int
    content: str


def update_content(
    payload: UpdateContentPayload,
):
    try:
        with Session(engine) as session:
            todo = session.get(Todos, id)
            print("🚀 ~ update_content ~ ", todo)

            if todo:
                todo.content = payload.content
                session.add(todo)
                session.commit()

                return (True, {"id": todo.id})

            return (False, "invalid id")
    except:
        print("🚀 ~ update_content ~ error")
        return (False, "database error")


def delete_todo(id: int):
    try:
        with Session(engine) as session:
            todo = session.exec(select(Todos).where(Todos.id == id)).first()
            if todo:
                session.delete(todo)
                session.commit()

                return (True, {"todo": todo})

        return (False, "invalid id")
    except:
        print("🚀 ~ update_content ~ error")
        return (False, "database error")
