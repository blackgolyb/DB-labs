from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task3(RunSQLFilesTask):
    """
    Lab 5 right join

    Дивимось яку оцінку в середньому студенти отримують на кожному факультеті
    """

    sql_files = [LAB_FOLDER / "right_join.sql"]
    migration_version = 1
    fill_function = fill_v3
