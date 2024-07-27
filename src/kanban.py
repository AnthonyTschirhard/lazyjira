from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static

from conductor import Conductor
from task_list import TaskList


class Kanban(Screen):
    """Kanban is the main view of the app"""

    widgets: list[TaskList]

    def __init__(
        self,
        conductor: Conductor,
    ):
        self.conductor = conductor

        self.widgets = []
        self.index_widgets = -1

        super().__init__()

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        infos = Static(
            "Lazy Jira, the best Jira TUI on the planet", classes="task-box"
        )
        infos.border_title = "[1] Status"
        yield infos

        details = Static("Two", classes="details-box")
        details.border_title = "Interesting Info"
        yield details

        sprint = TaskList(
            "[2] Sprint",
            ["Task 1", "Task 2", "Task 3", "Task 4"],
        )
        self.widgets.append(sprint)
        yield sprint

        backlog = TaskList(
            "[3] Backlog",
            ["Task 1", "Task 2", "Task 3", "Task 4"],
        )
        self.widgets.append(backlog)
        yield backlog

        self.next_group()

    def next_group(self):
        self.index_widgets = (
            (self.index_widgets + 1) % len(self.widgets)
        )
        self.widgets[self.index_widgets].focus()

    def previous_group(self):
        self.index_widgets = (
            (self.index_widgets - 1) % len(self.widgets)
        )
        self.widgets[self.index_widgets].focus()

    def next_task(self):
        self.widgets[self.index_widgets].next_task()

    def previous_task(self):
        self.widgets[self.index_widgets].previous_task()
