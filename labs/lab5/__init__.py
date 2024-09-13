from ..task import TaskGroup
from .task1 import Task1
from .task2 import Task2
from .task3 import Task3
from .task4 import Task4
from .task5 import Task5

lab = TaskGroup("lab 5")
lab.add_task(Task1("inner join"))
lab.add_task(Task2("left join"))
lab.add_task(Task3("right join"))
lab.add_task(Task4("full join"))
lab.add_task(Task5("cross join"))

__all__ = ["lab"]
