# from fastapi import  FastAPI #type: ignore
# import uvicorn  #type: ignore


# app = FastAPI()

# @app.get("/getTodos")
# def getTodos():
#     print("Get todos called")
#     return "get todos called"

# @app.post("/getTodos")
# def Post_Todos():
#     print("Post todos called")
#     return "Post todos called"


# @app.get("/getSingleTodos")
# def getSingleTodos():
#     print("Get Single todos called")
#     return "get Single todos called"

# @app.post("/getSingleTodos")
# def Post_SingleTodos():
#     print("Post Single todos called")
#     return "Post Single todos called"
# #Query Parameters
# @app.get("/getMultipleTodos")
# def getMultipleTodos(userName:str, rollNo:str):
#     print("Get Multiple todos called with query params", userName,rollNo)
#     return ("Get Multiple todos called with Query Params", userName,rollNo)
# #Dynamic Path Variable
# @app.post("/getMultipleTodos/{id}")
# def Post_MultipleTodos(id):
#     print("Post Multiple todos called",id)
#     return ("Post Multiple todos called with dynamic path variable" , id)

# def start():
#     uvicorn.run("todos.main:app", host="127.0.0.1" ,port=8080 , reload = True)
# ---------------------------------------------------------------------------------------


# Sql Model Fastapi Data Fetch And Connection With Postgres Database
# from fastapi import FastAPI # type: ignore
# import uvicorn  #type: ignore
# from sqlmodel import SQLModel, Session, select, Field, create_engine  # type: ignore

# app = FastAPI()
# connectionString = 'postgresql://postgres.ehzeojlysuxtslmbgvmd:FastApi_Practice@aws-0-ap-south-1.pooler.supabase.com:6543/postgres'
# connection = create_engine(connectionString)

# class Students(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     name: str
#     age: int
#     is_active:bool

# SQLModel.metadata.create_all(connection)

# @app.get("/getStudents")
# def getStudents():
#     with Session(connection) as session:
#         statement = select(Students).where(Students.name == 'Affan')
#         results = session.exec(statement)
#         data = results.all()
#         print(data)
#         return data

# def start():
#     uvicorn.run("todos.main:app", host="127.0.0.1" ,port=8080 , reload = True)

# ---------------------------------------------------------------------------------------


# Sql Model Fastapi Data Fetch And Connection With Postgres Database Client Side using query params
from fastapi import FastAPI, HTTPException
import uvicorn
from sqlmodel import Session, select
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

# class Students(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     name: str
#     age: int
#     is_active: bool

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


#  @app.put("/update_todo/{id}")
#     def update_todo(id:int ,todo: Update_Todos):
#      with Session(engine) as session:
#          db_todo = session.get(Todos, id)
#          if not db_todo:
#              raise HTTPException(status_code=404, detail="Todo not found")
#          todo_data = todo.model_dump(exclude_unset = True)
#          db_todo.sqlmodel_update(todo_data)
#          session.add(db_todo)
#          session.commit()
#          session.refresh(db_todo)
#          return {"status ": 200, "message ":" Todo updated successfully"}


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


# @app.get("/getStudents")
# def get_students(
#     id: int = Query(None),
#     name: str = Query(None),
#     age: int = Query(None)
# ):
#     with Session(connection) as session:
#         query = select(Students)

#         # Apply filters if parameters are provided
#         if id is not None:
#             query = query.where(Students.id == id)
#         if name is not None:
#             query = query.where(Students.name == name)
#         if age is not None:
#             query = query.where(Students.age == age)

#         results = session.exec(query)
#         data = results.all()
#         return data


def start():
    create_tables()
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8080, reload=True)
