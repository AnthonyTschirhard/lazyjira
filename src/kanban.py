from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static

from conductor import Conductor
from tasklist import TaskList


class Kanban(Screen):
    """The main view of the app"""

    AUTO_FOCUS = True

    def __init__(
        self,
        conductor: Conductor,
    ):
        self.conductor = conductor

        self.widgets = []
        self.index_widgets = 0

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

        sprint = TaskList("[2] Sprint")
        self.widgets.append(sprint)
        sprint.toggle()
        yield sprint

        backlog = TaskList("[3] Backlog")
        self.widgets.append(backlog)
        yield backlog

    def focus_next(self):
        self.widgets[self.index_widgets].toggle()
        self.index_widgets = (
            (self.index_widgets + 1) % len(self.widgets)
        )
        self.widgets[self.index_widgets].toggle()

    def focus_previous(self):
        self.widgets[self.index_widgets].toggle()
        self.index_widgets = (
            (self.index_widgets - 1) % len(self.widgets)
        )
        self.widgets[self.index_widgets].toggle()
