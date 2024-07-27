from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

from screen.kanban import Kanban
from conductor import Conductor
from client.jira_client import JiraClient


class LazyJiraApp(App):
    """A Textual app to make Jira bearable"""

    CSS_PATH = "grid_layout.tcss"

    TITLE = "Lazy JIRA"

    BINDINGS = [
        # ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit the app"),
        ("h", "previous_group", "Previous Section"),
        ("l", "next_group", "Next Section"),
        ("k", "previous_task", "Previous Task"),
        ("j", "next_task", "Next Task"),
    ]

    def __init__(
        self,
        conductor: Conductor,
    ):
        super().__init__()

        self.kanban = Kanban(conductor)

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()

        yield self.kanban

        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_next_group(self) -> None:
        self.kanban.next_group()
        self.refresh()

    def action_previous_group(self) -> None:
        self.kanban.previous_group()
        self.refresh()

    def action_next_task(self) -> None:
        self.kanban.next_task()
        self.refresh()

    def action_previous_task(self) -> None:
        self.kanban.previous_task()
        self.refresh()


if __name__ == "__main__":

    from envs import JIRA_USER, JIRA_TOKEN
    jira = JiraClient(JIRA_USER, JIRA_TOKEN)
    conductor = Conductor(jira)

    app = LazyJiraApp(conductor)
    app.run()
