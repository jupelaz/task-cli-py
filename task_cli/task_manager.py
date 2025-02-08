import sys
import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {task_id})')

def update_task(task_id, description):
    """Update an existing task."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} updated successfully')
            return
    print(f'Task {task_id} not found')

def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Task {task_id} deleted successfully')

def mark_task(task_id, status):
    """Mark a task as in-progress or done."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} marked as {status}')
            return
    print(f'Task {task_id} not found')

def list_tasks(status=None):
    """List tasks, optionally filtered by status."""
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created: {task['createdAt']}, Updated: {task['updatedAt']}")
