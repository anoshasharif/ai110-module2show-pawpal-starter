from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Anosha", "anosha@example.com")

dog = Pet("Biscuit", "Dog", 3)
cat = Pet("Mochi", "Cat", 2)

owner.add_pet(dog)
owner.add_pet(cat)

dog.add_task(Task("Evening walk", "daily", 30, 2, "18:00"))
dog.add_task(Task("Morning feeding", "daily", 10, 1, "08:00"))
cat.add_task(Task("Clean litter box", "daily", 15, 2, "08:00"))
cat.add_task(Task("Brush fur", "weekly", 20, 3, "14:00"))

scheduler = Scheduler()

for task in owner.get_all_tasks():
    scheduler.add_task(task)

print("Today's Schedule:")
for task in scheduler.generate_daily_plan():
    print(f"- {task.time} | {task.pet_name}: {task.title} ({task.duration} min, priority {task.priority})")

print("\nConflict Warnings:")
for warning in scheduler.detect_conflicts():
    print(warning)

print("\nTasks for Biscuit:")
for task in scheduler.filter_by_pet("Biscuit"):
    print(f"- {task.title}")

print("\nMarking first task complete and creating next recurring task:")
next_task = scheduler.mark_task_complete(scheduler.all_tasks[0])
if next_task:
    print(f"Created next task: {next_task.title} due on {next_task.due_date}")