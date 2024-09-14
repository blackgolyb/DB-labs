from functools import partial
from pathlib import Path
from typing import Callable
from textual.app import ComposeResult

from textual.widgets import Static, Button, Markdown, DataTable
from textual.containers import VerticalScroll
from textual.reactive import reactive
from textual.widget import Widget

from abc import abstractmethod

import logging

from labs.db import drop, get_table, migrate, run_sql_file

logger = logging.getLogger(__name__)


class Task(Widget):
    def __init__(self, name, description: str | None = None):
        super().__init__()
        self.task_name = name
        self.description = description or self.__doc__ or ""

    def get_name(self):
        return self.task_name

    @abstractmethod
    def compose(self) -> ComposeResult: ...


class DisplayTablesTask(Task):
    res = reactive(None, recompose=True)

    def compose(self):
        with VerticalScroll(id="content"):
            yield Markdown(self.description, id="tv-description")
            yield from self.get_control()
            if self.res is None:
                yield Static("No Result")
            else:
                yield from self.get_tables()

    def get_control(self):
        yield Button("Run", id="run")

    def get_tables(self):
        if len(self.res) == 0:
            yield Static("No Tables")
            return

        for table in self.res:
            w = DataTable()
            w.add_columns(*table[0])
            w.add_rows(table[1:])
            yield w

    @abstractmethod
    def run(self): ...

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "run":
            logger.debug("run")
            self.res = self.run()


class RunSQLFilesTask(DisplayTablesTask):
    sql_files: list[tuple[Path, bool] | Path] = []
    migration_version: int = -1
    need_drop: bool = True
    fill_function: Callable[[], None] = lambda: None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fill_function = partial(self.fill_function)

    @classmethod
    def fill(cls):
        cls.fill_function()

    def run(self):
        results = []

        if self.need_drop:
            drop()
            if self.migration_version >= 0:
                migrate(self.migration_version)

        self.fill()

        for command in self.sql_files:
            extract_table = True
            sql_file = None

            if isinstance(command, tuple):
                sql_file, extract_table = command
            else:
                sql_file = command

            res = run_sql_file(sql_file)
            if extract_table:
                results.append(get_table(res))

        return results


class TaskGroup:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __iter__(self):
        return iter(self.tasks)
