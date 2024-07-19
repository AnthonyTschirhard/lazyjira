from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static
from textual.scroll_view import ScrollableContainer


class TaskList(Screen):
    """The main view of the app"""

    def __init__(
        self,
        title: str,
        selected: bool = False,
    ):

        super().__init__()
        self.title = title
        self.selected = selected

    def compose(self) -> ComposeResult:
        """List of tasks"""

        task_list = ScrollableContainer(
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

        task_list.border_title = self.title
        if self.selected:
            task_list.add_class("selected")

        yield task_list
