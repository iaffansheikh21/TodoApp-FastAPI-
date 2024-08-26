from fastapi import  FastAPI #type: ignore
import uvicorn  #type: ignore


app = FastAPI()

@app.get("/getTodos")
def getTodos():
    print("Get todos called")
    return "get todos called"

@app.post("/getTodos")
def Post_Todos():
    print("Post todos called")
    return "Post todos called"


@app.get("/getSingleTodos")
def getSingleTodos():
    print("Get Single todos called")
    return "get Single todos called"

@app.post("/getSingleTodos")
def Post_SingleTodos():
    print("Post Single todos called")
    return "Post Single todos called"
#Query Parameters
@app.get("/getMultipleTodos")
def getMultipleTodos(userName:str, rollNo:str):
    print("Get Multiple todos called with query params", userName,rollNo)
    return ("Get Multiple todos called with Query Params", userName,rollNo)
#Dynamic Path Variable
@app.post("/getMultipleTodos/{id}")
def Post_MultipleTodos(id):
    print("Post Multiple todos called",id)
    return ("Post Multiple todos called with dynamic path variable" , id)

def start():
    uvicorn.run("todos.main:app", host="127.0.0.1" ,port=8080 , reload = True) 