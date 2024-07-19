from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

from conductor import Conductor
from jira_client import JiraClient
from kanban import Kanban


class LazyJiraApp(App):
    """A Textual app to make Jira bearable"""

    CSS_PATH = "grid_layout.tcss"

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit the app"),
    ]

    def __init__(
        self,
        conductor: Conductor,
    ):
        super().__init__()

        self.conductor = conductor

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()

        yield Kanban(self.conductor)

        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":

    from envs import JIRA_USER, JIRA_TOKEN
    jira = JiraClient(JIRA_USER, JIRA_TOKEN)
    conductor = Conductor(jira)

    app = LazyJiraApp(conductor)
    app.run()
