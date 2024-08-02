from textual.widgets import Static
from textual.widget import Widget


class TaskWidget(Widget):
    """A simple task object"""

    def __init__(
        self,
    ):
        super().__init__()

    def compose(self):
        # super().compose()
        yield Static("* ")
        yield Static("Task 1")
        yield Static("DR")
        yield Static("AB")
