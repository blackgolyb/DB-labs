from ..task import RunSQLFilesTask

from labs.db import fill_v2


class FillSecond(RunSQLFilesTask):
    """
    Helper for fill fist second of db
    """

    migration_version = 1
    fill_function = fill_v2
