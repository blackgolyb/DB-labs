from ..task import RunSQLFileTask
from labs.db import drop, get_table, migrate, run_sql_file, fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"

class Task4(RunSQLFileTask):
    """
    Lab 5 full join
    
    Дивимось які оцінки по яким предметам отримав студент та від якого викладача
    А також дивимось які студенти не були оцінені, та які викладачі жодного разу не оцінювали
    """

    def run(self):
        drop()
        migrate(1)
        fill_v3()
        res = get_table(run_sql_file(LAB_FOLDER / "full_join.sql"))

        return [res]
