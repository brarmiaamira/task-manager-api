
from fastapi import FastAPI

from database import create_table
from routers.tasks import router as tasks_router

app = FastAPI(
    title="Task Manager API",
    description="A REST API for managing tasks",
    version="1.0.0"
)

create_table()

app.include_router(tasks_router)


@app.get("/")
def home():
    return {"message": "Welcome to Task Manager API!"}


@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI!"}


@app.get("/info")
def info():
    return {
        "project name": "Task Manager API",
        "programming language": "Python"
    }
