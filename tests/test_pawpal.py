from pawpal_system import Task, Pet


def test_task_completion():
    task = Task("Walk", "daily", 30, 1)
    task.mark_done()
    assert task.completed is True


def test_add_task():
    pet = Pet("Biscuit", "Dog", 3)
    task = Task("Feed", "daily", 10, 1)

    pet.add_task(task)

    assert len(pet.tasks) == 1