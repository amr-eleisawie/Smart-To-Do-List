import gradio as gr
from core.task_manager import TaskManager

tm = TaskManager()

# تحويل المهام لنص
def format_tasks(tasks):
    if not tasks:
        return "No tasks yet"

    result = ""
    for t in tasks:
        result += f"{t['title']} | {t['priority']} | {t['status']}\n"
    return result

# عرض المهام
def show_tasks():
    return format_tasks(tm.get_tasks())

# إضافة مهمة
def add_task(task, priority):
    if task.strip() == "":
        return show_tasks()

    tm.add_task(task, priority)
    return show_tasks()

# تعليم المهمة كمكتملة
def mark_done(task_id):
    tm.mark_done(task_id)
    return show_tasks()

# حذف مهمة
def delete_task(task_id):
    tm.delete_task(task_id)
    return show_tasks()

# دالة الزر الجديد
def celebrate_success():
    return "True (U did it)"

# UI
with gr.Blocks() as app:
    gr.Markdown("## 📝 To-Do List App")

    task_input = gr.Textbox(label="Enter Task")
    priority = gr.Dropdown(["High", "Medium", "Low"], value="Medium")

    add_btn = gr.Button("Add Task")

    output = gr.Textbox(label="Tasks", lines=10)

    # زر الاحتفال الجديد
    celebrate_btn = gr.Button("🎉 Celebrate Success!")
    celebrate_output = gr.Textbox(label="Celebration Message", lines=2)

    # تحميل أولي
    app.load(show_tasks, outputs=output)

    add_btn.click(add_task, inputs=[task_input, priority], outputs=output)

    celebrate_btn.click(celebrate_success, outputs=celebrate_output)

app.launch()