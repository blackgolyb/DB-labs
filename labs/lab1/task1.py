from ..task import DisplayTablesTask

from labs.db import drop, migrate, fill_v1


class Task1(DisplayTablesTask):
    """
    Lab 1 Task 1 Create initial tables 
    """

    def run(self):
        drop()
        migrate(0)
        fill_v1()

        return []
