from datetime import date, timedelta
from pawpal_system import Task, Pet, Scheduler


def test_task_completion():
    task = Task("Walk", "daily", 30, 1, "08:00")
    task.mark_done()
    assert task.completed is True


def test_add_task():
    pet = Pet("Biscuit", "Dog", 3)
    task = Task("Feed", "daily", 10, 1, "09:00")
    pet.add_task(task)
    assert len(pet.tasks) == 1


def test_sort_by_time():
    scheduler = Scheduler()
    scheduler.add_task(Task("Evening walk", "daily", 30, 2, "18:00"))
    scheduler.add_task(Task("Morning feeding", "daily", 10, 1, "08:00"))
    scheduler.add_task(Task("Brush fur", "weekly", 20, 3, "14:00"))

    sorted_tasks = scheduler.sort_by_time()

    assert sorted_tasks[0].time == "08:00"
    assert sorted_tasks[1].time == "14:00"
    assert sorted_tasks[2].time == "18:00"


def test_recurring_daily_task():
    scheduler = Scheduler()
    task = Task("Morning feeding", "daily", 10, 1, "08:00", due_date=date.today())
    scheduler.add_task(task)

    new_task = scheduler.mark_task_complete(task)

    assert task.completed is True
    assert new_task is not None
    assert new_task.due_date == date.today() + timedelta(days=1)


def test_conflict_detection():
    scheduler = Scheduler()
    scheduler.add_task(Task("Morning feeding", "daily", 10, 1, "08:00"))
    scheduler.add_task(Task("Clean litter box", "daily", 15, 2, "08:00"))

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "08:00" in conflicts[0]