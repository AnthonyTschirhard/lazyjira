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

        sprint = TaskList(
            "[2] Sprint",
            ["Task 1", "Task 2", "Task 3", "Task 4"]
        )
        self.widgets.append(sprint)
        sprint.toggle()
        yield sprint

        backlog = TaskList(
            "[3] Backlog",
            ["Task 1", "Task 2", "Task 3", "Task 4"]
        )
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

    # def on_button_pressed(self, event: Button.Pressed) -> None:
    #     """Event handler called when a button is pressed."""
    #     button_id = event.button.id
    #     time_display = self.query_one(TimeDisplay)
    #     if button_id == "start":
    #         time_display.start()
    #         self.add_class("started")
    #     elif button_id == "stop":
    #         time_display.stop()
    #         self.remove_class("started")
    #     elif button_id == "reset":
    #         time_display.reset()
