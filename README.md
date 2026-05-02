# Smart To-Do List App

A modern, user-friendly to-do list application built with Gradio and Python. Manage your tasks efficiently with priority levels and task status tracking.

## Features

- ✅ **Add Tasks** - Create new tasks with different priority levels (High, Medium, Low)
- 📋 **View Tasks** - See all your tasks in a clean, organized format
- ✔️ **Mark Complete** - Mark tasks as done when you finish them
- ❌ **Delete Tasks** - Remove tasks you no longer need
- 💾 **Persistent Storage** - Tasks are saved to JSON for data persistence
- 🎨 **Web Interface** - Beautiful Gradio-based web UI

## Project Structure

```
app/
├── app.py                          # Main application entry point
├── students.json                   # Student data storage
├── core/
│   ├── __init__.py                # Package initialization
│   ├── APP_InterFace.py            # Gradio web interface
│   └── task_manager.py             # Task management logic
├── data/
│   └── tasks.json                  # Task data storage
└── README.md                       # This file
```

## Installation

### Prerequisites

- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/amr-eleisawie/Smart-To-Do-List.git
cd Smart-To-Do-List
```

2. Install required dependencies:
```bash
pip install gradio
```

3. Run the application:
```bash
python core/APP_InterFace.py
```

The app will launch at `http://127.0.0.1:7860`

## Usage

### Adding a Task
1. Enter your task in the "Enter Task" text field
2. Select a priority level from the dropdown (High, Medium, Low)
3. Click the "Add Task" button
4. Your task will appear in the Tasks display

### Viewing Tasks
Tasks are displayed in a table format showing:
- Task title
- Priority level
- Current status (Pending/Done)

### Marking Tasks Complete
Click the "✅ Done" button next to any task to mark it as complete

### Deleting Tasks
Click the "❌ Delete" button next to any task to remove it

## Technical Details

### TaskManager Class
The `TaskManager` class handles all task operations:
- `add_task(title, priority)` - Add a new task
- `get_tasks()` - Retrieve all tasks
- `mark_done(task_id)` - Mark a task as complete
- `delete_task(task_id)` - Remove a task
- `save_tasks()` - Persist tasks to JSON file

### Data Storage
Tasks are stored in `data/tasks.json` with the following structure:
```json
[
  {
    "id": 1,
    "title": "Task name",
    "priority": "High",
    "status": "Pending",
    "created_at": "2026-05-02T10:30:00.000000"
  }
]
```

## Dependencies

- **Gradio** - Web interface framework for machine learning models and data applications
- **Python Standard Library** - json, os, datetime modules

## Contributing

Feel free to fork this repository and submit pull requests for any improvements!

## License

This project is open source and available under the MIT License.

## Author

[Amr Eleisawie](https://github.com/amr-eleisawie)

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Last Updated:** May 2, 2026
