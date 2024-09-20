from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task3(RunSQLFilesTask):
    """
    Lab 8

    Виводимо кількість груп та кількість студентів на факультеті для тих факультетів де кількість студентів > 2
    """

    sql_files = [LAB_FOLDER / "function_3.sql"]
    migration_version = 4
    fill_function = fill_v3
