from ..task import TaskGroup
from .task1 import Task1

lab = TaskGroup("lab 1")
lab.add_task(Task1("create tables"))

__all__ = ["lab"]
