from ..task import RunSQLFilesTask
from labs.db import fill_v3
from labs.config import SQL_FOLDER

LAB_FOLDER = SQL_FOLDER / "queries"


class Task4(RunSQLFilesTask):
    """
    Lab 5 full join

    Дивимось які оцінки по яким предметам отримав студент та від якого викладача
    А також дивимось які студенти не були оцінені, та які викладачі жодного разу не оцінювали
    """

    sql_files = [LAB_FOLDER / "full_join.sql"]
    migration_version = 1
    fill_function = fill_v3
