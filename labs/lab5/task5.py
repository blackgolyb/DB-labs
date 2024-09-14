from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task5(RunSQLFilesTask):
    """
    Lab 5 cross join

    Дивимось оцінки по кожному предмету для кожного студента
    """

    sql_files = [LAB_FOLDER / "cross_join.sql"]
    migration_version = 1
    fill_function = fill_v3
