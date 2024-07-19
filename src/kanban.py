from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static
from textual.scroll_view import ScrollableContainer

from conductor import Conductor
from tasklist import TaskList


class Kanban(Screen):
    """The main view of the app"""

    def __init__(
        self,
        conductor: Conductor,
    ):
        self.conductor = conductor

        self.widgets = []
        self.index_widgets = 2

        super().__init__()

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        infos = Static(
            "Lazy Jira, the best Jira TUI on the planet", classes="task-box"
        )
        infos.border_title = "[1] Status"
        self.widgets.append(infos)
        yield infos

        details = Static("Two", classes="details-box")
        details.border_title = "Interesting Info"
        self.widgets.append(details)
        yield details

        sprint = TaskList("[2] Sprint")
        yield sprint
        sprint.on_focus()

        backlog = TaskList("[3] Backlog")
        self.widgets.append(backlog)
        yield backlog

    def focus_next(self):
        # super().focus_next()
        self.widgets[self.index_widgets].on_blur()
        self.index_widgets += 1
        self.widgets[self.index_widgets].on_focus()
