import gradio as gr
from core.task_manager import TaskManager

tm = TaskManager()

# عرض المهام بشكل أوضح + ID
def format_tasks(tasks):
    if not tasks:
        return "No tasks yet"

    result = ""
    for t in tasks:
        status = "✅" if t["status"] == "Done" else "⏳"
        result += f"{status} {t['title']} ({t['priority']})\nID: {t['id']}\n\n"
    return result

# عرض المهام
def show_tasks():
    return format_tasks(tm.get_tasks())

# إضافة مهمة
def add_task(task, priority):
    if task.strip() == "":
        return show_tasks(), ""

    tm.add_task(task, priority)
    return show_tasks(), ""  # تفريغ input

# تعليم المهمة كمكتملة
def mark_done(task_id):
    try:
        task_id = int(task_id)
        tm.mark_done(task_id)
    except ValueError:
        pass  # Invalid ID, do nothing
    return show_tasks()

# حذف مهمة
def delete_task(task_id):
    try:
        task_id = int(task_id)
        tm.delete_task(task_id)
    except ValueError:
        pass  # Invalid ID, do nothing
    return show_tasks()

# زر الاحتفال
def celebrate_success():
    for task in tm.tasks:
        task["status"] = "Done"
    tm.save_tasks()
    return show_tasks(), "🔥 Great job! Keep going!"

# إعادة تعيين التطبيق
def reset_app():
    tm.tasks = []
    tm.save_tasks()
    return show_tasks()

# UI
with gr.Blocks() as app:
    gr.Markdown("## 📝 To-Do List App")

    task_input = gr.Textbox(label="Enter Task")
    priority = gr.Dropdown(["High", "Medium", "Low"], value="Medium")

    add_btn = gr.Button("Add Task")

    output = gr.Textbox(label="Tasks", lines=15)

    # إدخال ID
    task_id_input = gr.Textbox(label="Enter Task ID")

    done_btn = gr.Button("✅")
    delete_btn = gr.Button("❌")

    # زر الاحتفال
    celebrate_btn = gr.Button("🎉 Celebrate Success!")
    celebrate_output = gr.Textbox(label="Celebration Message", lines=2)

    # زر إعادة التعيين
    reset_btn = gr.Button("Reset App")

    # تحميل أولي
    app.load(show_tasks, outputs=output)

    add_btn.click(add_task, inputs=[task_input, priority], outputs=[output, task_input])

    done_btn.click(mark_done, inputs=task_id_input, outputs=output)
    delete_btn.click(delete_task, inputs=task_id_input, outputs=output)

    celebrate_btn.click(celebrate_success, outputs=[output, celebrate_output])

    reset_btn.click(reset_app, outputs=output)

app.launch()