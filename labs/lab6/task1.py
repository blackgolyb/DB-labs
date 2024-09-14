from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task1(RunSQLFilesTask):
    """
    Lab 6

    Виводимо таблицю оцінок з додатковою колонкою ECTS
    """

    sql_files = [LAB_FOLDER / "view_1.sql"]
    migration_version = 2
    fill_function = fill_v3
