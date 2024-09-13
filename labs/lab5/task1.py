from ..task import RunSQLFileTask
from labs.db import drop, get_table, migrate, run_sql_file, fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"

class Task1(RunSQLFileTask):
    """
    Lab 5 inner join
    
    Дивимось списки груп
    """

    def run(self):
        drop()
        migrate(1)
        fill_v3()
        res = get_table(run_sql_file(LAB_FOLDER / "inner_join.sql"))

        return [res]
