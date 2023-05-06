from typing import Annotated
from fastapi import APIRouter, Body, HTTPException
from .services import (
    TodoItem,
    UpdateContentPayload,
    get_all_todos,
    get_todo,
    create_one_todo,
    update_content,
    delete_todo,
)

todos_router = APIRouter(prefix="/todos", tags=["todos"])


@todos_router.post("")
def create_one_todo_controller(todoItem: TodoItem):
    print("🚀 ~ create_one_todo_handler:")
    res = create_one_todo(todoItem)
    if res[0] == False:
        raise HTTPException(status_code=500, detail={"ok": False, "reason": res[1]})
    return {"ok": True, "data": res[1]}


@todos_router.get("")
def get_all_todos_controller():
    print("🚀 ~ get_all_todos_controller:")

    res = get_all_todos()
    if res[0] == False:
        raise HTTPException(status_code=500, detail={"ok": False, "reason": res[1]})
    return {"ok": True, "data": res[1]}


@todos_router.get("/:id")
def get_todo_controller(id: int):
    print("🚀 ~ get_todo_controller:")

    res = get_todo(id)
    if res[0] == False:
        raise HTTPException(status_code=500, detail={"ok": False, "reason": res[1]})
    return {"ok": True, "data": res[1]}


@todos_router.delete("/:id")
def delete_todo_controller(id: int):
    print("🚀 ~ delete_todo_controller:")
    res = delete_todo(id)

    if res[0] == False:
        raise HTTPException(
            status_code=res[1] == "database error" if 500 else 400,
            detail={"ok": False, "reason": res[1]},
        )
    return {"ok": True, "data": res[1]}


@todos_router.patch("/:id/content")
def update_content_controller(content: Annotated[str, Body()], id: int):
    print("🚀 ~ update_content_controller:")
    payload = UpdateContentPayload(content=content, id=id)
    res = update_content(payload)

    if res[0] == False:
        raise HTTPException(
            status_code=res[1] == "database error" if 500 else 400,
            detail={"ok": False, "reason": res[1]},
        )
    return {"ok": True, "data": res[1]}
