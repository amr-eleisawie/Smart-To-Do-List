import streamlit as st
from core.task_manager import TaskManager

# init
tm = TaskManager()

st.title("🧠 Smart To-Do List")

# ------------------------
# ➕ Add Task
# ------------------------
st.subheader("Add New Task")

title = st.text_input("Task Title")
priority = st.selectbox("Priority", ["Low", "Medium", "High"])

if st.button("Add Task"):
    if title:
        tm.add_task(title, priority)
        st.success("Task added!")
        st.rerun()
    else:
        st.error("Please enter a task")

# ------------------------
# 📋 Show Tasks
# ------------------------
st.subheader("Your Tasks")

tasks = tm.get_tasks()

for task in tasks:
    col1, col2, col3, col4 = st.columns([4,2,2,2])

    with col1:
        if task["status"] == "Done":
            st.markdown(f"~~{task['title']}~~")
        else:
            st.write(task["title"])

    with col2:
        st.write(task["priority"])

    with col3:
        if st.button("✅ Done", key=f"done_{task['id']}"):
            tm.mark_done(task["id"])
            st.rerun()

    with col4:
        if st.button("❌ Delete", key=f"del_{task['id']}"):
            tm.delete_task(task["id"])
            st.rerun()