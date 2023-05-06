from sqlmodel import SQLModel
from .models import *
from .engine import engine

# if this file is run by itself, not imported this function will run
if __name__ == "main":
    print("i have been called")

    def db_setup():
        SQLModel.metadata.create_all(engine)

    db_setup()
