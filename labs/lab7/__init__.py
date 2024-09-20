from ..task import TaskGroup
from .task2 import Task2
from .task3 import Task3
from .task4 import Task4

lab = TaskGroup("lab 7")
lab.add_task(Task2("add teacher"))
lab.add_task(Task3("count group students"))
lab.add_task(Task4("get student info"))

__all__ = ["lab"]
