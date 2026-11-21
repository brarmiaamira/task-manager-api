
from fastapi import APIRouter, HTTPException

from schemas import Task
from database import (insert_task,get_all_tasks,get_task_by_id,update_task_in_db,delete_task_from_db,filter_tasks,search_tasks)

router = APIRouter()


@router.post("/tasks")
def create_task(task: Task):
    task_id = insert_task(task)

    return {
        "message": "Task created successfully!",
        "task_id": task_id}
@router.get("/tasks")
def get_tasks():
    return get_all_tasks()
@router.get("/tasks/filter")
def filter_tasks_endpoint(status: str = None,priority: str = None):
    return filter_tasks(status, priority)
@router.get("/tasks/search")
def search_tasks_endpoint(keyword: str):
    if not keyword.strip():
        raise HTTPException(
            status_code=400,
            detail="Search keyword cannot be empty"
        )

    return search_tasks(keyword)


@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    success = update_task_in_db(task_id, updated_task)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task updated successfully!",
        "task": get_task_by_id(task_id)
    }


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    success = delete_task_from_db(task_id)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {"message": "Task deleted successfully!"}
