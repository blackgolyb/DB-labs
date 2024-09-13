from ..task import RunSQLFileTask

from labs.db import drop, fill_v2, migrate


class FillSecond(RunSQLFileTask):
    """
    Helper for fill fist second of db
    """

    def run(self):
        drop()
        migrate(1)
        fill_v2()

        return []
