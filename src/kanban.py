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
        self.index_widgets = None

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
        self.widgets.append(sprint)
        sprint.toggle()
        self.index_widgets = 2
        yield sprint

        backlog = TaskList("[3] Backlog")
        self.widgets.append(backlog)
        backlog.focus()
        yield backlog

    def focus_next(self):
        self.widgets[self.index_widgets].toggle()
        self.index_widgets += 1
        self.widgets[self.index_widgets].toggle()
        print(self.widgets)

    def focus_previous(self):
        self.widgets[self.index_widgets].toggle()
        self.index_widgets -= 1
        self.widgets[self.index_widgets].toggle()
        print(self.widgets)
