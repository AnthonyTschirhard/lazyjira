from textual.app import App

from screen.kanban import Kanban
from conductor import Conductor
from client.jira_client import JiraClient
from client.db_client import DBClient


class LazyJiraApp(App):
    """A Textual app to make Jira bearable"""

    CSS_PATH = "grid_layout.tcss"

    TITLE = "Lazy JIRA"

    BINDINGS = [
        ("q", "quit", "Quit the app"),
    ]

    def __init__(
        self,
        conductor: Conductor,
    ):
        super().__init__()

        self.kanban = Kanban(conductor)

    def on_mount(self):
        self.push_screen(self.kanban)


if __name__ == "__main__":

    from envs import JIRA_USER, JIRA_TOKEN
    jira_client = JiraClient(JIRA_USER, JIRA_TOKEN)
    db_client = DBClient()
    conductor = Conductor(jira_client, db_client)

    app = LazyJiraApp(conductor)
    app.run()
