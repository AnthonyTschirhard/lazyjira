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
        self.initial_index = 1
        self.index = 0

        self.title = TASK_LISTS[list_name]["title"]

        self.border_title = self.title

    def next_task(self):
        self.index += 1
        self.scroll_to_center(self.highlighted_child)

    def previous_task(self):
        self.index -= 1
        self.scroll_to_center(self.highlighted_child)
