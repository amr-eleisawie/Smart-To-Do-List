import gradio as gr
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from app import TaskManager

tm = TaskManager()

# عرض المهام
def show_tasks():
    tasks = tm.get_tasks()
    return "\n".join(tasks) if tasks else "No tasks yet"

# إضافة مهمة
def add_task(task):
    if task.strip() == "":
        return show_tasks()
    
    tm.add_task(task)
    return show_tasks()

# واجهة Gradio
with gr.Blocks() as app:
    gr.Markdown("## 📝 To-Do List App")

    task_input = gr.Textbox(label="Enter Task")
    add_btn = gr.Button("Add Task")

    output = gr.Textbox(label="Tasks", lines=10)

    # تحميل أولي
    app.load(show_tasks, outputs=output)

    # عند الضغط على الزر
    add_btn.click(add_task, inputs=task_input, outputs=output)

app.launch()