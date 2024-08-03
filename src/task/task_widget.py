from textual.widgets import Static
from textual.widgets import Static

from task import BaseTask


class TaskWidget(Static):
    """A simple task object"""

    def __init__(
        self,
        task: BaseTask,
    ):
        super().__init__()
        self.task_ = task

    def compose(self):
        yield Static(self.task_.summary)
