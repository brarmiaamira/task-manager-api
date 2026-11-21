from enum import Enum
from pydantic import BaseModel

class TaskStatus(str, Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"

class TaskPriority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Task(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus
    priority: TaskPriority