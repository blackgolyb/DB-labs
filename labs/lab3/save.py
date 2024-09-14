from ..task import DisplayTablesTask
from labs.db import drop, migrate, fill_v2, save
from labs.config import PROJECT_FOLDER, ALL_TABLES

class Save(DisplayTablesTask):
    """
    Lab 3 Export data to CSV file
    """
    
    def run(self):
        drop()
        migrate(1)
        fill_v2()
        save(ALL_TABLES, PROJECT_FOLDER / "dump")
        
        return []
