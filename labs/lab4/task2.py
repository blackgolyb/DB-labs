from ..task import RunSQLFilesTask
from labs.db import fill_v2
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task2(RunSQLFilesTask):
    """
    Lab 4 group select
    """

    sql_files = [LAB_FOLDER / "count_students_per_group.sql"]
    migration_version = 1
    fill_function = fill_v2
