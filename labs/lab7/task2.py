from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task2(RunSQLFilesTask):
    """
    Lab 7

    Показуємо як працює процедура для додання нового викладача
    """

    sql_files = [
        LAB_FOLDER / "get_teachers_sort.sql",
        (LAB_FOLDER / "procedure_2.sql", False),
        LAB_FOLDER / "get_teachers_sort.sql",
    ]
    migration_version = 3
    fill_function = fill_v3
