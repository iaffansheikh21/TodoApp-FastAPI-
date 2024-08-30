# Sql Model Fastapi Data Fetch And Connection With Postgres Database Client Side using query params
from fastapi import FastAPI, HTTPException  
from fastapi.middleware.cors import CORSMiddleware  
import uvicorn  
from sqlmodel import Session, select  
from dotenv import load_dotenv 

load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .config.db import create_tables, engine
from .models.todos import Todos, Update_Todos


@app.get("/get_todos")
def get_todos():
    with Session(engine) as session:
        statement = select(Todos)
        results = session.exec(statement)
        data = results.all()
        print(data)
        return data


@app.post("/create_todo")
def create_todo(todo: Todos):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return {"status ": 200, "message ": " Todo created successfully"}


@app.put("/update_todo/{id}")
def update_todo(id: int, todo: Update_Todos):
    with Session(engine) as session:
        db_todo = session.get(Todos, id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        todo_data = todo.model_dump(exclude_unset=True)
        db_todo.sqlmodel_update(todo_data)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return {"status": 200, "message": "todo updated successfully"}


@app.delete("/delete_todo/{todo_id}")
def delete_todo(todo_id: int):
    with Session(engine) as session:
        print(todo_id)
        db_todo = session.get(Todos, todo_id)
        print(db_todo)

        if not db_todo:
            raise HTTPException(status_code=404, detail="Todo not found")

        session.delete(db_todo)
        session.commit()

        return {"status": 200, "message": "Todo deleted successfully"}


def start():
    create_tables()
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8080, reload=True)
