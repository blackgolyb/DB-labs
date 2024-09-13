from ..task import TaskGroup
from .drop import DropAll
from .fill1 import FillFirst
from .fill2 import FillSecond
from .fill3 import FillJoin

utils = TaskGroup("utils")
utils.add_task(DropAll("drop"))
utils.add_task(FillFirst("fill v1"))
utils.add_task(FillSecond("fill v2"))
utils.add_task(FillJoin("fill v3"))

__all__ = ["utils"]
