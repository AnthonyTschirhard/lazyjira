from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.scroll_view import ScrollableContainer

from conductor import Conductor
from jira_client import JiraClient


class LazyJiraApp(App):
    """A Textual app to manage stopwatches."""
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

        infos = Static(
            "Lazy Jira, the best Jira TUI on the planet", classes="task-box"
        )
        infos.border_title = "[1] Status"
        yield infos

        details = Static("Two", classes="details-box")
        details.border_title = "Interesting Info"
        yield details

        sprint = ScrollableContainer(
            *[
                Static(name)
                for name in [
                    "TASK 1",
                    "TASK 2",
                    "TASK 3",
                    "TASK 4",
                    "TASK 5",
                ]
            ], classes="task-box selected"
        )
        sprint.border_title = "[2] Sprint"
        yield sprint

        backlog = ScrollableContainer(
            *[
                Static(name)
                for name in [
                    "TASK 1",
                    "TASK 2",
                    "TASK 3",
                    "TASK 4",
                    "TASK 5",
                ]
            ], classes="task-box"
        )
        backlog.border_title = "[3] Backlog"
        yield backlog

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
