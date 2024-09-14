from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task2(RunSQLFilesTask):
    """
    Lab 6

    Виводимо усі оцінки які є оцікною 'A' в ECTS
    """

    sql_files = [LAB_FOLDER / "view_2.sql"]
    migration_version = 2
    fill_function = fill_v3
