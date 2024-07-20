from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

from conductor import Conductor
from jira_client import JiraClient
from kanban import Kanban


class LazyJiraApp(App):
    """A Textual app to make Jira bearable"""

    CSS_PATH = "grid_layout.tcss"

    TITLE = "Lazy JIRA"

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit the app"),
        ("h", "focus_previous", "Focus Previous"),
        ("l", "focus_next", "Focus Next"),
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

    def action_focus_next(self) -> None:
        self.kanban.focus_next()
        self.refresh()

    def action_focus_previous(self) -> None:
        self.kanban.focus_previous()
        self.refresh()


if __name__ == "__main__":

    from envs import JIRA_USER, JIRA_TOKEN
    jira = JiraClient(JIRA_USER, JIRA_TOKEN)
    conductor = Conductor(jira)

    app = LazyJiraApp(conductor)
    app.run()
