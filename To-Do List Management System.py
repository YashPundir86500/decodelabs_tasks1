"""
============================================================
  To-Do List Management System
  Storage : tasks.json (persistent across restarts)
============================================================
"""

import json
import os

# ── Constant ──────────────────────────────────────────────
TASKS_FILE = "tasks.json"


# ══════════════════════════════════════════════════════════
#  Load & Save Tasks
# ══════════════════════════════════════════════════════════

def load_tasks():
    """Load tasks from JSON file."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Warning: Could not read tasks file. Starting fresh.")
    return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    try:
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f, indent=2)
    except IOError as e:
        print(f"Warning: Could not save tasks: {e}")


# ══════════════════════════════════════════════════════════
#  Helper – Next ID
# ══════════════════════════════════════════════════════════

def next_id(tasks):
    """Generate next unique task ID."""
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


# ══════════════════════════════════════════════════════════
#  1. Add Task
# ══════════════════════════════════════════════════════════

def add_task(tasks):
    """
    INPUT  : task name from user
    PROCESS: create dict and append to list
    OUTPUT : confirmation message
    """
    print("\n--- Add Task ---")
    name = input("Enter task: ").strip()

    if not name:
        print("Error: Task cannot be empty.")
        return

    task = {
        "id"    : next_id(tasks),
        "task"  : name,
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task #{task['id']} added: \"{name}\"")


# ══════════════════════════════════════════════════════════
#  2. View Tasks
# ══════════════════════════════════════════════════════════

def view_tasks(tasks):
    """
    INPUT  : task list
    PROCESS: format and print each task
    OUTPUT : table + summary
    """
    print("\n--- All Tasks ---")

    if not tasks:
        print("No tasks yet. Add one with option 1.")
        return

    print(f"  {'No.':<5} {'Status':<12} Task")
    print("  " + "-" * 50)

    for i, t in enumerate(tasks, start=1):
        icon = "[DONE]" if t["status"] == "Completed" else "[    ]"
        print(f"  {i:<5} {icon}  {t['task']}")

    total     = len(tasks)
    completed = sum(1 for t in tasks if t["status"] == "Completed")
    pending   = total - completed

    print("  " + "-" * 50)
    print(f"  Total: {total}  |  Completed: {completed}  |  Pending: {pending}")


# ══════════════════════════════════════════════════════════
#  3. Delete Task
# ══════════════════════════════════════════════════════════

def delete_task(tasks):
    """
    INPUT  : serial number from user
    PROCESS: validate and remove from list
    OUTPUT : confirmation or error
    """
    view_tasks(tasks)
    if not tasks:
        return

    print("\n--- Delete Task ---")
    raw = input("Enter task number to delete (0 to cancel): ").strip()

    if not raw.lstrip("-").isdigit():
        print("Error: Please enter a valid number.")
        return

    choice = int(raw)
    if choice == 0:
        print("Cancelled.")
        return
    if choice < 1 or choice > len(tasks):
        print(f"Error: Enter a number between 1 and {len(tasks)}.")
        return

    removed = tasks.pop(choice - 1)
    save_tasks(tasks)
    print(f"Deleted: \"{removed['task']}\"")


# ══════════════════════════════════════════════════════════
#  4. Mark Task as Completed
# ══════════════════════════════════════════════════════════

def mark_completed(tasks):
    """
    INPUT  : serial number from user
    PROCESS: set status to 'Completed'
    OUTPUT : confirmation or error
    """
    view_tasks(tasks)
    if not tasks:
        return

    print("\n--- Mark as Completed ---")
    raw = input("Enter task number to mark complete (0 to cancel): ").strip()

    if not raw.lstrip("-").isdigit():
        print("Error: Please enter a valid number.")
        return

    choice = int(raw)
    if choice == 0:
        print("Cancelled.")
        return
    if choice < 1 or choice > len(tasks):
        print(f"Error: Enter a number between 1 and {len(tasks)}.")
        return

    task = tasks[choice - 1]
    if task["status"] == "Completed":
        print(f"Task #{choice} is already completed.")
        return

    task["status"] = "Completed"
    save_tasks(tasks)
    print(f"Task #{choice} marked as Completed: \"{task['task']}\"")


# ══════════════════════════════════════════════════════════
#  Menu
# ══════════════════════════════════════════════════════════

def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("       TO-DO LIST MANAGER")
    print("=" * 40)
    print("  1. Add Task")
    print("  2. View Tasks")
    print("  3. Delete Task")
    print("  4. Mark Task as Completed")
    print("  5. Exit")
    print("-" * 40)


# ══════════════════════════════════════════════════════════
#  Main
# ══════════════════════════════════════════════════════════

def main():
    """Main loop – runs until user selects Exit."""
    tasks = load_tasks()
    print(f"Welcome! ({len(tasks)} task(s) loaded)")

    while True:
        show_menu()
        choice = input("  Enter choice (1-5): ").strip()

        if   choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            print("\nGoodbye! Tasks saved.\n")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


# ── Entry Point ────────────────────────────────────────────
if __name__ == "__main__":
    main()