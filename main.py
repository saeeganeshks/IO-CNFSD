from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import date

app = FastAPI()

class Task(BaseModel) :
    task_name: str
    due_date : str

@app.get("/")
def basic() :
    return "Hello, Welcome to Daily Task App!"

@app.get("/today")
def today():
    today = date.today()
    return "Today's date:",today

@app.get("/tasks")
def today_tasks():
    tasks = [{1:'Task A'},{2:'Task B'},{3:'Task c'}]
    return "Today's Tasks",tasks

@app.post("/newtask")
def new_task(task_var: Task):
    task_encoded = jsonable_encoder(task_var)
    ntask = task_encoded['task_name']
    due = task_encoded['due_date']
    return "Task: {}, due on {}".format(ntask,due)


@app.post("/changetask")
def del_task(task_var: Task):
    task_encoded = jsonable_encoder(task_var)
    ntask = task_encoded['task_name']
    due = task_encoded['due_date']
    return "Task Changed"
