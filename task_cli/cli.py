import argparse
from task_cli.task_manager import add_task, update_task, delete_task, mark_task, list_tasks

def main():
    parser = argparse.ArgumentParser(description="Task CLI Application")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("task_id", type=int, help="Task ID")
    update_parser.add_argument("description", type=str, help="New task description")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="Task ID")

    mark_parser = subparsers.add_parser("mark", help="Mark task as in-progress or done")
    mark_parser.add_argument("task_id", type=int, help="Task ID")
    mark_parser.add_argument("status", choices=["in-progress", "done"], help="Task status")

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--status", type=str, help="Filter tasks by status", required=False)

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.task_id, args.description)
    elif args.command == "delete":
        delete_task(args.task_id)
    elif args.command == "mark":
        mark_task(args.task_id, args.status)
    elif args.command == "list":
        list_tasks(args.status)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()