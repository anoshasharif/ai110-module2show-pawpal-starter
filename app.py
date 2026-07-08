import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan", "jordan@example.com")

st.subheader("Owner Info")
owner_name = st.text_input("Owner name", value=st.session_state.owner.name)

if st.button("Save owner"):
    st.session_state.owner.name = owner_name
    st.success("Owner saved!")

st.divider()

st.subheader("Add a Pet")

pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
age = st.number_input("Pet age", min_value=0, max_value=30, value=2)

if st.button("Add pet"):
    new_pet = Pet(pet_name, species, int(age))
    st.session_state.owner.add_pet(new_pet)
    st.success(f"Added {pet_name}!")

if st.session_state.owner.pets:
    st.write("Current pets:")
    for pet in st.session_state.owner.pets:
        st.write(f"- {pet.name} ({pet.species}, age {pet.age})")
else:
    st.info("No pets yet.")

st.divider()

st.subheader("Add a Task")

if st.session_state.owner.pets:
    pet_names = [pet.name for pet in st.session_state.owner.pets]
    selected_pet_name = st.selectbox("Choose pet", pet_names)

    task_title = st.text_input("Task title", value="Morning walk")
    frequency = st.selectbox("Frequency", ["daily", "weekly", "monthly"])
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    priority = st.selectbox("Priority", [1, 2, 3], index=0)

    if st.button("Add task"):
        selected_pet = None
        for pet in st.session_state.owner.pets:
            if pet.name == selected_pet_name:
                selected_pet = pet

        if selected_pet:
            new_task = Task(task_title, frequency, int(duration), int(priority))
            selected_pet.add_task(new_task)
            st.success(f"Added task '{task_title}' for {selected_pet.name}!")

else:
    st.info("Add a pet before adding tasks.")

st.divider()

st.subheader("Current Tasks")

all_tasks = st.session_state.owner.get_all_tasks()

if all_tasks:
    task_rows = []
    for task in all_tasks:
        task_rows.append(
            {
                "Task": task.title,
                "Frequency": task.frequency,
                "Duration": task.duration,
                "Priority": task.priority,
                "Completed": task.completed,
            }
        )
    st.table(task_rows)
else:
    st.info("No tasks yet.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    scheduler = Scheduler()

    for task in st.session_state.owner.get_all_tasks():
        scheduler.add_task(task)

    plan = scheduler.generate_daily_plan()

    if plan:
        st.write("Today's Schedule:")
        for i, task in enumerate(plan, start=1):
            st.write(f"{i}. {task.title} - {task.duration} min - priority {task.priority}")
    else:
        st.info("No tasks to schedule.")
