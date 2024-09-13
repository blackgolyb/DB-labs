from ..task import TaskGroup
from .task1 import Task1
from .task2 import Task2
from .task3 import Task3

lab = TaskGroup("lab 6")
lab.add_task(Task1("ects"))
lab.add_task(Task2("best grade"))
lab.add_task(Task3("student info"))

__all__ = ["lab"]
