from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task1(RunSQLFilesTask):
    """
    Lab 8

    Виводимо кількість студентів для кожної групи з використанням збереженої функції 
    """

    sql_files = [LAB_FOLDER / "function_1.sql"]
    migration_version = 4
    fill_function = fill_v3
