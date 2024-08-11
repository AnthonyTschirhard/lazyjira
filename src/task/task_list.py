from textual.widgets import ListItem, ListView

from task import TaskWidget, BaseTask

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

    BINDINGS = [
        ("k", "cursor_up", "Previous Task"),
        ("j", "cursor_down", "Next Task"),
    ]

    def __init__(
        self,
        list_name: str,
        tasks_list: list[BaseTask]
    ):

        self.items = [
            ListItem(TaskWidget(
                task
            ))
            for task in tasks_list
        ]
        super().__init__(*self.items, classes="task-box")

        self.border_title = TASK_LISTS[list_name]["title"]
