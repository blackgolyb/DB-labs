from ..task import RunSQLFileTask

from labs.db import drop, fill_v1, migrate


class FillFirst(RunSQLFileTask):
    """
    Helper for fill fist version of db
    """

    def run(self):
        drop()
        migrate(0)
        fill_v1()

        return []
