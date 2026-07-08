"""PawPal+ — pet care application (backend logic).

This file defines the four core classes for the app:
    Owner, Pet, Task, Scheduler

Pet and Task are dataclasses (they mostly hold data).
Owner and Scheduler are regular classes (they have more behavior).
"""

from dataclasses import dataclass, field


@dataclass
class Task:
    """A single care task for a pet (e.g. "Walk", "Feed")."""

    title: str
    frequency: str          # how often, e.g. "daily", "weekly"
    duration: int           # how long the task takes, in minutes
    priority: int           # ranking value (1 = most important)
    completed: bool = False

    def mark_done(self) -> None:
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    """A pet that belongs to an owner and has care tasks."""

    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.tasks.append(task)


class Owner:
    """A pet owner who can have one or more pets."""

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.pets: list = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's list of pets."""
        self.pets.append(pet)

    def list_pets(self) -> list:
        """Return the owner's pets."""
        return self.pets

    def get_all_tasks(self) -> list:
        """Collect and return the tasks from every pet the owner has."""
        all_tasks = []
        for pet in self.pets:
            # Add each pet's tasks to the combined list.
            for task in pet.tasks:
                all_tasks.append(task)
        return all_tasks


class Scheduler:
    """Collects and organizes tasks across all pets."""

    def __init__(self) -> None:
        self.all_tasks: list = []

    def add_task(self, task: Task) -> None:
        """Add a task to the scheduler."""
        self.all_tasks.append(task)

    def get_due_tasks(self) -> list:
        """Return the tasks that still need to be done (not completed yet)."""
        due = []
        for task in self.all_tasks:
            if not task.completed:
                due.append(task)
        return due

    def sort_by_priority(self) -> list:
        """Return all tasks sorted by priority (1 = most important first)."""
        # sorted() does not change the original list; it returns a new one.
        return sorted(self.all_tasks, key=lambda task: task.priority)

    def sort_by_frequency(self) -> list:
        """Return all tasks sorted alphabetically by how often they occur."""
        return sorted(self.all_tasks, key=lambda task: task.frequency)

    def generate_daily_plan(self) -> list:
        """Build an ordered plan of the tasks still due, most important first.

        Steps:
            1. Keep only the tasks that are not completed yet.
            2. Sort those tasks by priority (1 = most important).
        """
        # 1. Start from the tasks that still need doing.
        due_tasks = self.get_due_tasks()
        # 2. Order them so the most important task comes first.
        daily_plan = sorted(due_tasks, key=lambda task: task.priority)
        return daily_plan
