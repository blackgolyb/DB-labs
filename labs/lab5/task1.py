from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task1(RunSQLFilesTask):
    """
    Lab 5 inner join

    Дивимось списки груп
    """

    sql_files = [LAB_FOLDER / "inner_join.sql"]
    migration_version = 1
    fill_function = fill_v3
