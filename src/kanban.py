from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static
from textual.scroll_view import ScrollableContainer

from conductor import Conductor


class Kanban(Screen):
    """The main view of the app"""

    def __init__(
        self,
        conductor: Conductor,
    ):
        self.conductor = conductor
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

        sprint = ScrollableContainer(
            *[
                Static(name)
                for name in [
                    "TASK 1",
                    "TASK 2",
                    "TASK 3",
                    "TASK 4",
                    "TASK 5",
                ]
            ], classes="task-box selected"
        )
        sprint.border_title = "[2] Sprint"
        yield sprint

        backlog = ScrollableContainer(
            *[
                Static(name)
                for name in [
                    "TASK 1",
                    "TASK 2",
                    "TASK 3",
                    "TASK 4",
                    "TASK 5",
                ]
            ], classes="task-box"
        )
        backlog.border_title = "[3] Backlog"
        yield backlog
