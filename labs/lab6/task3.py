from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task3(RunSQLFilesTask):
    """
    Lab 6

    Виводимо детальну інформацію про кожного студента
    """

    sql_files = [LAB_FOLDER / "view_3.sql"]
    migration_version = 2
    fill_function = fill_v3
