import pytest
from task_cli.task_manager import add_task, update_task, delete_task, list_tasks

def test_add_task():
    add_task("Test task")
    tasks = list_tasks()
    assert any(task['description'] == "Test task" for task in tasks)

def test_update_task():
    add_task("Old task")
    update_task(1, "Updated task")
    tasks = list_tasks()
    assert any(task['description'] == "Updated task" for task in tasks)

def test_delete_task():
    add_task("To be deleted")
    delete_task(1)
    tasks = list_tasks()
    assert not any(task['description'] == "To be deleted" for task in tasks)