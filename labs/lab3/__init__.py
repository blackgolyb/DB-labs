from ..task import TaskGroup
from .save import Save
from .load import Load

lab = TaskGroup("lab 3")
lab.add_task(Save("export to csv"))
lab.add_task(Load("import from csv"))

__all__ = ["lab"]
