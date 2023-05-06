from enum import Enum
from typing import Optional
from sqlmodel import Field, SQLModel


class TodosTypes(str, Enum):
    personal = "personal"
    business = "business"


class Todos(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    type: TodosTypes = Field(default=TodosTypes.business)
