import logging

from ..task import DisplayTablesTask
from labs.db import drop, migrate, fill_v1, run_sql_file, get_table
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"
logger = logging.getLogger(__name__)


class Task1(DisplayTablesTask):
    """
    Lab 2 Task 1 Migrate to student profile
    
    create One-To-One relationship between Student and Profile
    """

    def run(self):
        drop()
        migrate(0)
        fill_v1()
        students_before = get_table(run_sql_file(LAB_FOLDER / "get_students.sql"))
        migrate(1, 1)
        students_after = get_table(run_sql_file(LAB_FOLDER / "get_students.sql"))
        profiles = get_table(run_sql_file(LAB_FOLDER / "get_students_profiles.sql"))

        return [students_before, students_after, profiles]
