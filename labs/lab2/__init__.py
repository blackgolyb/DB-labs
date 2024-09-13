from ..task import TaskGroup
from .task1 import Task1
from .task2 import Task2

lab = TaskGroup("lab 2")
lab.add_task(Task1("migrate to profile"))
lab.add_task(Task2("downgrade profile"))

__all__ = ["lab"]
