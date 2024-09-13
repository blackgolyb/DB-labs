from textual.app import ComposeResult, App as BaseApp
from textual.containers import Container, Horizontal
from textual.widgets import Tree, Static
from textual.reactive import reactive

from labs.task import Task
from .lab1 import lab as lab1
from .lab2 import lab as lab2
from .lab3 import lab as lab3
from .lab4 import lab as lab4
from .lab5 import lab as lab5
from .lab6 import lab as lab6
from .utils import utils


class TaskView(Static):
    current_task = reactive[Task | None](None, recompose=True)

    def compose(self) -> ComposeResult:
        if self.current_task is None:
            yield Static("No task selected")
            return

        with Container(id="content"):
            yield self.current_task

    async def load(self, task: Task):
        self.current_task = task


class App(BaseApp):
    CSS = """
    Screen {
        align: center middle;
        layers: main max;
    }
    
    #tasks-view {
        width: 1fr;
        height: 100%;
    }
    
    #sidebar {
        width: 30;
        height: 100%;
    }
    """

    def __init__(self, tasks):
        super().__init__()
        self.tasks = tasks
        self.test = False

    def compose(self) -> ComposeResult:
        with Horizontal(id="app-layout"):
            with Container(id="sidebar"):
                yield self.create_tasks_tree()

            yield TaskView(id="tasks-view")

    def create_tasks(self, tasks, root_node):
        for task_group in tasks:
            group_node = root_node.add(task_group.name, expand=False)
            for task in task_group:
                group_node.add_leaf(task.get_name(), task)

    def create_tasks_tree(self):
        tree = Tree("Tasks", id="tasks-list")
        tree.root.expand()

        if len(self.tasks) == 1:
            tree.show_root = False

        for topic in self.tasks:
            topic_node = tree.root.add(topic, expand=True)
            self.create_tasks(self.tasks[topic], topic_node)

        return tree

    async def _on_tree_node_selected(self, message: Tree.NodeSelected) -> None:
        node_data = message.node.data
        if isinstance(node_data, Task):
            await self.query_one("#tasks-view").load(node_data) # type: ignore


def create_app() -> App:
    tasks = [
        utils,
        lab1,
        lab2,
        lab3,
        lab4,
        lab5,
        lab6,
    ]
    return App({"labs": tasks})
