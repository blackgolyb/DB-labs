from ..task import RunSQLFilesTask
from labs.db import fill_v2
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task1(RunSQLFilesTask):
    """
    Lab 4 basic select
    """

    sql_files = [LAB_FOLDER / "get_groups.sql"]
    migration_version = 1
    fill_function = fill_v2
