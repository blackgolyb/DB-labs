from ..task import RunSQLFileTask
from labs.db import drop, get_table, migrate, load, run_sql_file
from labs.config import SQL_FOLDER, PROJECT_FOLDER, ALL_TABLES

LAB_FOLDER = SQL_FOLDER / "queries"

class Load(RunSQLFileTask):
    """
    Lab 3 Expoort data to CSV file
    """

    def run(self):
        drop()
        migrate(1)
        before = get_table(run_sql_file(LAB_FOLDER / "get_students_profiles.sql"))
        load(ALL_TABLES, PROJECT_FOLDER / "dump")
        after = get_table(run_sql_file(LAB_FOLDER / "get_students_profiles.sql"))

        return [before, after]
