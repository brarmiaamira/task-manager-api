import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent / "tasks.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection
def create_table():

    connection=get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL,
            priority TEXT NOT NULL)""")

    connection.commit()
    connection.close()
def insert_task(task):
    connection=get_connection()
    cursor=connection.execute("""INSERT INTO Tasks(title,description,status,priority) VALUES (?,?,?,?)""",(task.title,task.description,task.status.value,task.priority.value))
    connection.commit()
    task_id = cursor.lastrowid
    connection.close()
    return task_id
def get_all_tasks():
    connection = get_connection()
    cursor = connection.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    connection.close()
    return [dict(task) for task in tasks]
def get_task_by_id(task_id):
    connection = get_connection()
    cursor = connection.execute("SELECT * FROM tasks WHERE id = ?",(task_id,))
    task = cursor.fetchone()
    connection.close()
    if task is None:
        return None
    return dict(task)
def update_task_in_db(task_id, updated_task):
    connection = get_connection()
    cursor = connection.execute("""UPDATE tasks SET title = ?, description = ?, status = ?, priority = ?WHERE id = ?""", (updated_task.title,updated_task.description,updated_task.status.value,updated_task.priority.value,task_id))
    connection.commit()
    updated = cursor.rowcount > 0
    connection.close()
    return updated
def delete_task_from_db(task_id):
    connection = get_connection()
    cursor = connection.execute("DELETE FROM tasks WHERE id = ?",(task_id,))
    connection.commit()
    deleted = cursor.rowcount > 0
    connection.close()
    return deleted
def filter_tasks(status=None, priority=None):
    connection = get_connection()
    query = "SELECT * FROM tasks WHERE 1=1"
    parameters = []
    if status:
        query += " AND status = ?"
        parameters.append(status)
    if priority:
        query += " AND priority = ?"
        parameters.append(priority)
    cursor = connection.execute(query, parameters)
    tasks = cursor.fetchall()
    connection.close()
    return [dict(task) for task in tasks]
def search_tasks(keyword):
    connection = get_connection()
    cursor = connection.execute("SELECT * FROM tasks WHERE title LIKE ?",(f"%{keyword}%",))
    tasks = cursor.fetchall()
    connection.close()
    return [dict(task) for task in tasks]