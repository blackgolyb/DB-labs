from ..task import TaskGroup
from .task1 import Task1
from .task2 import Task2
from .task3 import Task3

lab = TaskGroup("lab 8")
lab.add_task(Task1("count groups students"))
lab.add_task(Task2("filter group"))
lab.add_task(Task3("filter faculty"))

__all__ = ["lab"]
