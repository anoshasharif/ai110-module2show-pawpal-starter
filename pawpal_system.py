"""PawPal+ — pet care application (backend logic).

This file defines the four core classes for the app:
    Owner, Pet, Task, Scheduler

Pet and Task are dataclasses (they mostly hold data).
Owner and Scheduler are regular classes (they have more behavior).
"""

from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    """A single pet care task."""

    title: str
    frequency: str
    duration: int
    priority: int
    time: str = "09:00"
    pet_name: str = ""
    due_date: date = field(default_factory=date.today)
    completed: bool = False

    def mark_done(self) -> None:
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    """A pet that has care tasks."""

    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        task.pet_name = self.name
        self.tasks.append(task)


class Owner:
    """A pet owner with one or more pets."""

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.pets = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner."""
        self.pets.append(pet)

    def list_pets(self) -> list:
        """Return all pets."""
        return self.pets

    def get_all_tasks(self) -> list:
        """Return all tasks from all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


class Scheduler:
    """Organizes pet care tasks."""

    def __init__(self) -> None:
        self.all_tasks = []

    def add_task(self, task: Task) -> None:
        """Add a task to the scheduler."""
        self.all_tasks.append(task)

    def get_due_tasks(self) -> list:
        """Return unfinished tasks."""
        return [task for task in self.all_tasks if not task.completed]

    def sort_by_priority(self) -> list:
        """Sort tasks by priority."""
        return sorted(self.all_tasks, key=lambda task: task.priority)

    def sort_by_time(self) -> list:
        """Sort tasks by time in HH:MM format."""
        return sorted(self.all_tasks, key=lambda task: task.time)

    def filter_by_status(self, completed: bool) -> list:
        """Filter tasks by completion status."""
        return [task for task in self.all_tasks if task.completed == completed]

    def filter_by_pet(self, pet_name: str) -> list:
        """Filter tasks by pet name."""
        return [task for task in self.all_tasks if task.pet_name == pet_name]

    def mark_task_complete(self, task: Task) -> Task | None:
        """Complete a task and create the next recurring task if needed."""
        task.mark_done()

        if task.frequency == "daily":
            next_date = task.due_date + timedelta(days=1)
        elif task.frequency == "weekly":
            next_date = task.due_date + timedelta(weeks=1)
        else:
            return None

        new_task = Task(
            task.title,
            task.frequency,
            task.duration,
            task.priority,
            task.time,
            task.pet_name,
            next_date,
        )
        self.add_task(new_task)
        return new_task

    def detect_conflicts(self) -> list:
        """Detect tasks scheduled at the same time."""
        warnings = []
        seen = {}

        for task in self.all_tasks:
            if task.time in seen:
                warnings.append(
                    f"Conflict: '{task.title}' and '{seen[task.time]}' are both scheduled at {task.time}."
                )
            else:
                seen[task.time] = task.title

        return warnings

    def generate_daily_plan(self) -> list:
        """Generate today's plan sorted by time."""
        return self.sort_by_time()