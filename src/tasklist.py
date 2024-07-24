from textual.widgets import Static, ListItem, ListView


class TaskList(ListView):
    """The Kingdom of tasks"""

    def __init__(
        self,
        title: str,
        task_names: list[str]
    ):

        self.items = [
            ListItem(Static(name))
            for name in task_names
        ]
        super().__init__(*self.items, classes="task-box")
        self.initial_index = 1
        self.index = 0

        self.title = title

        self.border_title = self.title

    def next_task(self):
        print("Next Task")
        self.index += 1

    def previous_task(self):
        print("Previous Task")
        self.index -= 1
