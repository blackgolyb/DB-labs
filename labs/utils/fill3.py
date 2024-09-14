from ..task import RunSQLFilesTask

from labs.db import fill_v3


class FillJoin(RunSQLFilesTask):
    """
    Helper for test join queries
    """

    migration_version = 2
    fill_function = fill_v3
