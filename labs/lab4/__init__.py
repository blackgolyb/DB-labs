from ..task import TaskGroup
from .task1 import Task1
from .task2 import Task2
from .task3 import Task3
from .task4 import Task4

lab = TaskGroup("lab 4")
lab.add_task(Task1("basic select"))
lab.add_task(Task2("group select"))
lab.add_task(Task3("sort select"))
lab.add_task(Task4("where select"))

__all__ = ["lab"]
