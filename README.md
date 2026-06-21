# ✅ To-Do List Management System

A simple yet powerful command-line To-Do List Manager written in Python. Tasks are saved persistently using a `tasks.json` file, so your data is never lost between sessions.

---

## 📸 Preview

```
========================================
       TO-DO LIST MANAGER
========================================
  1. Add Task
  2. View Tasks
  3. Delete Task
  4. Mark Task as Completed
  5. Exit
----------------------------------------
  Enter choice (1-5):
```

---

## 🚀 Features

- **Add Tasks** – Quickly add new tasks with a name
- **View Tasks** – See all tasks with their completion status and a summary
- **Delete Tasks** – Remove tasks by their serial number
- **Mark as Completed** – Update task status to `Completed`
- **Persistent Storage** – All tasks are auto-saved to `tasks.json`

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed (uses only built-in modules)

---

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/todo-list-manager.git
   cd todo-list-manager
   ```

2. **Run the script**
   ```bash
   python To-Do List Management System.py
   ```

---

## 📁 Project Structure

```
todo-list-manager/
│
├──  To-Do List Management System.py   # Main application file
├── tasks.json       # Auto-generated task storage (created on first run)
└── README.md        # Project documentation
```

---

## 💾 How Data is Stored

Tasks are stored in a local `tasks.json` file in the following format:

```json
[
  {
    "id": 1,
    "task": "Buy groceries",
    "status": "Pending"
  },
  {
    "id": 2,
    "task": "Complete assignment",
    "status": "Completed"
  }
]
```

---

## 📋 Usage Guide

| Option | Action |
|--------|--------|
| `1` | Add a new task |
| `2` | View all tasks with status |
| `3` | Delete a task by number |
| `4` | Mark a task as completed |
| `5` | Exit the program |

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
