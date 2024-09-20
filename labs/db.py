import csv
from functools import lru_cache
from pathlib import Path
import logging

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session

from labs.config import SQL_FOLDER, MIGRATONS_FOLDER, get_settings


logger = logging.getLogger(__name__)


@lru_cache
def get_sessionmaker():
    settings = get_settings()
    engine = create_engine(
        url=settings.db.url_str,
        echo=True,
    )
    return sessionmaker(engine)


def get_session() -> Session:
    return get_sessionmaker()()


def run_sql_file(filename: Path):
    query = filename.read_text()
    with get_session() as session:
        res = session.execute(text(query))
        session.commit()

    return res


def run_sql_file_service(session, filename: Path):
    query = filename.read_text()
    return session.execute(text(query))


def run_sql_test(query: str):
    with get_session() as session:
        res = session.execute(text(query))
        session.commit()

    return res


def get_table(query):
    keys = query.keys()
    rows = query.all()
    return (keys, *rows)


def save(table_names: list[str], dump_folder: Path):
    if not dump_folder.exists():
        dump_folder.mkdir(parents=True, exist_ok=True)

    for table_name in table_names:
        filename = dump_folder / f"{table_name}.csv"
        query = f"SELECT * FROM {table_name}"
        res = get_table(run_sql_test(query))

        with filename.open("w", newline="") as csvfile:
            w = csv.writer(csvfile)
            for row in res:
                w.writerow(map(str, row))


def load(table_names: list[str], dump_folder: Path):
    if not dump_folder.exists():
        raise ValueError("dump_folder does not exist")

    for table_name in table_names:
        filename = dump_folder / f"{table_name}.csv"
        rows = []
        with filename.open("r", newline="") as csvfile:
            r = csv.reader(csvfile)
            for row in r:
                rows.append(row)

        def to_tuple(row, to_string=True):
            if to_string:
                row = map(lambda t: f"\'{t}\'", row)
            return f'({", ".join(row)})'
        
        values = ", ".join(map(to_tuple, rows[1:]))
        names = to_tuple(rows[0], False)
        query = f"INSERT INTO {table_name} {names} VALUES {values};"
        run_sql_test(query)


def drop():
    run_sql_file(SQL_FOLDER / "drop.sql")


def migrate(version: int, start: int = 0):
    migrations = []

    for child in MIGRATONS_FOLDER.iterdir():
        if child.is_dir():
            prefix = child.name.split("_")[0]
            try:
                parsed_prefix = int(prefix)
            except ValueError:
                continue

            if (
                not (child / "upgrade.sql").exists()
                or not (child / "downgrade.sql").exists()
            ):
                continue

            migrations.append((parsed_prefix, child))

    migrations.sort(key=lambda x: x[0])
    if len(migrations) <= version:
        return False

    for i in range(start, version + 1):
        run_sql_file(migrations[i][1] / "upgrade.sql")

    return True


def fill_v1():
    run_sql_file(SQL_FOLDER / "fill_v1.sql")


def fill_v2():
    run_sql_file(SQL_FOLDER / "fill_v2.sql")
    
def fill_v3():
    run_sql_file(SQL_FOLDER / "fill_v3.sql")
