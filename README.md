# Task Manager API

A RESTful API built with Python and FastAPI to manage tasks. It supports creating, retrieving, updating, deleting, filtering, and searching tasks.

## Features

- Create new tasks
- Retrieve all tasks or a specific task
- Update existing tasks
- Delete tasks
- Filter tasks by status and priority
- Search tasks by title
- Validate input data using Pydantic
- Handle HTTP errors
- Store tasks in an SQLite database
- Automated testing with Pytest

## Technologies Used

- Python
- FastAPI
- Pydantic
- SQLite
- Pytest
- HTTPX

## Project Structure

```text
task-manager-api/
├── main.py
├── database.py
├── schemas.py
├── routers/
│   └── tasks.py
├── tests/
│   └── test_main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project:

```bash
cd task-manager-api
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate it on Windows:

```powershell
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## Run Tests

```bash
python -m pytest -v
```

## Database

The application uses SQLite. The database and its `tasks` table are initialized automatically when the application starts.

## Learning Goals

This project was built to practice REST API development, data validation, database integration, CRUD operations, and automated testing with FastAPI.