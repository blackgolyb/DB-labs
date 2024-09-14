from ..task import RunSQLFilesTask
from labs.db import fill_v2
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task3(RunSQLFilesTask):
    """
    Lab 4 sort select
    """

    sql_files = [LAB_FOLDER / "get_teachers_sort.sql"]
    migration_version = 1
    fill_function = fill_v2
