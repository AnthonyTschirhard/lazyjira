from textual.widgets import ListItem, ListView

from task.task_compound import TaskCompound

TASK_LISTS = {
    "sprint": {
        "title": "[2] Sprint"
    },
    "backlog": {
        "title": "[3] Backlog"
    },
}


class TaskList(ListView):
    """The Kingdom of tasks"""

    def __init__(
        self,
        list_name: str,
    ):

        self.items = [
            ListItem(TaskCompound())
            for name in [1, 2, 3, 4]
        ]
        super().__init__(*self.items, classes="task-box")
        self.initial_index = 1
        self.index = 0

        self.title = TASK_LISTS[list_name]["title"]

        self.border_title = self.title

    def next_task(self):
        print("Next Task")
        self.index += 1

    def previous_task(self):
        print("Previous Task")
        self.index -= 1
