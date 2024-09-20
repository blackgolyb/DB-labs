from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task3(RunSQLFilesTask):
    """
    Lab 7

    Показуємо як працює процедура для отримання кількості студентів в групі
    """

    sql_files = [
        (LAB_FOLDER / "procedure_3_1.sql", False),
        (LAB_FOLDER / "procedure_3_2.sql", True),
    ]
    migration_version = 3
    fill_function = fill_v3
