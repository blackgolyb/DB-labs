from ..task import RunSQLFileTask

from labs.db import drop, fill_v3, migrate


class FillJoin(RunSQLFileTask):
    """
    Helper for fill fist second of db
    """

    def run(self):
        drop()
        migrate(1)
        fill_v3()

        return []
