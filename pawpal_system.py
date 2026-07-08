"""PawPal+ — pet care application (class skeleton).

This file defines the four core classes for the app:
    Owner, Pet, Task, Scheduler

Pet and Task are dataclasses (they mostly hold data).
Owner and Scheduler are regular classes (they have more behavior).

No scheduling or business logic is implemented yet — the method
bodies are stubs that use `pass`.
"""

from dataclasses import dataclass, field


@dataclass
class Task:
    """A single care task for a pet (e.g. "Walk", "Feed")."""

    title: str
    frequency: str          # how often, e.g. "daily", "weekly"
    duration: int           # how long the task takes, in minutes
    priority: int           # ranking value the scheduler sorts by
    completed: bool = False

    def mark_done(self) -> None:
        """Mark this task as completed."""
        pass


@dataclass
class Pet:
    """A pet that belongs to an owner and has care tasks."""

    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        pass


class Owner:
    """A pet owner who can have one or more pets."""

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.pets: list = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's list of pets."""
        pass

    def list_pets(self) -> list:
        """Return the owner's pets."""
        pass


class Scheduler:
    """Collects and organizes tasks across all pets."""

    def __init__(self) -> None:
        self.all_tasks: list = []

    def add_task(self, task: Task) -> None:
        """Add a task to the scheduler."""
        pass

    def get_due_tasks(self) -> list:
        """Return the tasks that are currently due."""
        pass

    def sort_by_frequency(self) -> list:
        """Return the tasks sorted by how often they occur."""
        pass

    def generate_daily_plan(self) -> list:
        """Build an ordered plan of tasks for the day."""
        pass
