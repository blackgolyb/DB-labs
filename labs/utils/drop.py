from ..task import RunSQLFileTask

from labs.db import run_sql_file
from labs.config import SQL_FOLDER


class DropAll(RunSQLFileTask):
    """
    Helper for droop all tables 
    """

    def run(self):
        run_sql_file(SQL_FOLDER / "drop.sql")
        
        return []
