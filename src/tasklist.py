from textual.app import ComposeResult
from textual.widgets import Static
from textual.widget import Widget
from textual.scroll_view import ScrollableContainer


class TaskList(Widget):
    """The main view of the app"""

    def __init__(
        self,
        title: str,
    ):

        super().__init__()
        self.title = title

        self.task_container = ScrollableContainer(
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

        self.task_container.border_title = self.title

    def compose(self) -> ComposeResult:
        """List of tasks"""
        yield self.task_container

    def toggle(self) -> None:
        self.task_container.toggle_class("selected")
