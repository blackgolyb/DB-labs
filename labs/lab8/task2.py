from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task2(RunSQLFilesTask):
    """
    Lab 8

    Виводимо ті групи в яких кількість студентів більша ніж 1 збереженої функції для фільтрації 
    """

    sql_files = [LAB_FOLDER / "function_2.sql"]
    migration_version = 4
    fill_function = fill_v3
