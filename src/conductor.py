from jira_client import JiraClient
from db_client import DBClient


class Conductor():

    def __init__(
        self,
        jira_client: JiraClient,
        db_client: DBClient,
    ):
        self.jira_client = jira_client
        self.db_client = db_client

    def sync_jira_local(self):
        pass

    def get_jira_issues(self):
        return self.jira_client.get_my_issues()

    def get_db_issues(self):
        return self.db_client.get_tasks()


if __name__ == "__main__":
    from envs import JIRA_USER, JIRA_TOKEN

    jira_client = JiraClient(JIRA_USER, JIRA_TOKEN)
    db_client = DBClient()

    conductor = Conductor(jira_client, db_client)
    issues = conductor.get_db_issues()
