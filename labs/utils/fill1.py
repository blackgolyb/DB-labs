from ..task import RunSQLFilesTask

from labs.db import fill_v1


class FillFirst(RunSQLFilesTask):
    """
    Helper for fill fist version of db
    """

    migration_version = 0
    fill_function = fill_v1
