from textual.app import ComposeResult
from textual.screen import Screen
from textual.events import Focus, Blur
from textual.widgets import Static
from textual.scroll_view import ScrollableContainer


class TaskList(Screen):
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

    def on_focus(self) -> None:
        self.task_container.add_class("selected")

    def on_blur(self) -> None:
        self.task_list.remove_class("selected")
