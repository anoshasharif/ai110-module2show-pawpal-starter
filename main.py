from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Anosha", "anosha@example.com")

pet1 = Pet("Biscuit", "Dog", 3)
pet2 = Pet("Mittens", "Cat", 5)

owner.add_pet(pet1)
owner.add_pet(pet2)

pet1.add_task(Task("Morning walk", "daily", 30, 1))
pet1.add_task(Task("Feeding", "daily", 10, 1))
pet2.add_task(Task("Clean litter box", "daily", 15, 2))
pet2.add_task(Task("Brush fur", "weekly", 20, 3))

scheduler = Scheduler()

for task in owner.get_all_tasks():
    scheduler.add_task(task)

daily_plan = scheduler.generate_daily_plan()

print("Today's Schedule:")
for i, task in enumerate(daily_plan, start=1):
    print(f"{i}. {task.title} - {task.duration} min - priority {task.priority}")