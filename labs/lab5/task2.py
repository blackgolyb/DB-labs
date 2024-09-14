from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task2(RunSQLFilesTask):
    """
    Lab 5 left join

    Дивимось яку середню оцінку факультет ставить студентам
    """

    sql_files = [LAB_FOLDER / "left_join.sql"]
    migration_version = 1
    fill_function = fill_v3
