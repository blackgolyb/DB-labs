from ..task import RunSQLFileTask
from labs.db import drop, get_table, migrate, run_sql_file, fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"

class Task3(RunSQLFileTask):
    """
    Lab 6
    
    Виводимо детальну інформацію про кожного студента
    """

    def run(self):
        drop()
        migrate(2)
        fill_v3()
        res = get_table(run_sql_file(LAB_FOLDER / "view_3.sql"))

        return [res]
