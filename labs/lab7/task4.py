from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task4(RunSQLFilesTask):
    """
    Lab 7

    Показуємо як працює процедура для отримання детальної інформації по студенту
    """

    sql_files = [
        (LAB_FOLDER / "procedure_4_1.sql", False),
        (LAB_FOLDER / "procedure_4_2.sql", True),
    ]
    migration_version = 3
    fill_function = fill_v3
