from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static

from conductor import Conductor
from task.task_list import TaskList


class Kanban(Screen):
    """Kanban is the main view of the app"""

    widgets: list[TaskList]

    def __init__(
        self,
        conductor: Conductor,
    ):
        self.conductor = conductor
        self.conductor.sync_jira_local()

        self.widgets = []
        self.index_widgets = -1

        super().__init__()

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        infos = Static(
            "Lazy Jira, Jira made fun", classes="task-box"
        )
        infos.border_title = "[1] Status"
        yield infos

        details = Static("", classes="details-box")
        details.border_title = "Details"
        yield details

        sprint = TaskList(
            "sprint",
            self.conductor.get_db_issues(
                in_sprint=True,
                filter_done=False,
            )
        )
        self.widgets.append(sprint)
        yield sprint

        backlog = TaskList(
            "backlog",
            self.conductor.get_db_issues(
                in_sprint=False,
                filter_done=True,
            )
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
