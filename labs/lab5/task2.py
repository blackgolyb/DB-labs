from ..task import RunSQLFileTask
from labs.db import drop, get_table, migrate, run_sql_file, fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"

class Task2(RunSQLFileTask):
    """
    Lab 5 left join
    
    Дивимось яку середню оцінку факультет ставить студентам
    """

    def run(self):
        drop()
        migrate(1)
        fill_v3()
        res = get_table(run_sql_file(LAB_FOLDER / "left_join.sql"))

        return [res]
