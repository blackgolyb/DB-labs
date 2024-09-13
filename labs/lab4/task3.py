from ..task import RunSQLFileTask
from labs.db import drop, get_table, migrate, run_sql_file, fill_v2
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"

class Task3(RunSQLFileTask):
    """
    Lab 4 sort select
    """

    def run(self):
        drop()
        migrate(1)
        fill_v2()
        groups = get_table(run_sql_file(LAB_FOLDER / "get_teachers_sort.sql"))

        return [groups]
