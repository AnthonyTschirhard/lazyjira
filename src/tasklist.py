from textual.widgets import Static, ListItem, ListView


class TaskList(ListView):
    """The Kingdom of tasks"""

    def __init__(
        self,
        title: str,
        task_names: list[str]
    ):

        super().__init__(
            *[
                ListItem(ListItem(Static(name)))
                for name in task_names
            ]
        )
        self.title = title

        self.border_title = self.title

        self.add_class("task-box")

    def toggle(self) -> None:
        self.toggle_class("selected")
