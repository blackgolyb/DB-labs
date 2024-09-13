import logging

from ..task import RunSQLFileTask
from labs.db import drop, migrate, fill_v2, run_sql_file, get_table
from labs.config import SQL_FOLDER, MIGRATONS_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"
logger = logging.getLogger(__name__)


class Task2(RunSQLFileTask):
    """
    Lab 2 Task 2 Downgrade student profile
    """

    def run(self):
        drop()
        migrate(1)
        fill_v2()
        profiles = get_table(run_sql_file(LAB_FOLDER / "get_students_profiles.sql"))
        students_before = get_table(run_sql_file(LAB_FOLDER / "get_students.sql"))
        run_sql_file(MIGRATONS_FOLDER / "0001_create_student_profile" / "downgrade.sql")
        students_after = get_table(run_sql_file(LAB_FOLDER / "get_students.sql"))

        return [students_before, profiles, students_after]
        return [students_before, profiles]
