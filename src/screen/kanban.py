from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer

from conductor import Conductor
from task.task_list import TaskList


class Kanban(Screen):
    """Kanban is the main view of the app"""

    widgets: list[TaskList]

    BINDINGS = [
        ("l", "focus_next_group", "Next Group"),
        ("h", "focus_previous_group", "Previous Group"),
    ]

    def __init__(
        self,
        conductor: Conductor,
    ):
        self.conductor = conductor
        # self.conductor.sync_jira_local()

        super().__init__()

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()

        infos = Static(
            "Lazy Jira, Jira made fun", classes="task-box",
        )
        infos.border_title = "Status"
        yield infos

        details = Static("", classes="details-box")
        details.border_title = "Details"
        yield details

        sprint = TaskList(
            "Sprint",
            self.conductor.get_db_issues(
                in_sprint=True,
                filter_done=False,
            )
        )
        yield sprint

        backlog = TaskList(
            "Backlog",
            self.conductor.get_db_issues(
                in_sprint=False,
                filter_done=True,
            )
        )
        yield backlog

        yield Footer()

    def action_focus_next_group(self) -> None:
        self.focus_next(TaskList)

    def action_focus_previous_group(self) -> None:
        self.focus_previous(TaskList)
