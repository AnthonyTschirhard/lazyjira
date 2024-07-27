from task import JiraTask
from jira_client import JiraClient


class Conductor():

    def __init__(
        self,
        jira: JiraClient,
    ):
        self.jira = jira

    def sync_jira_local(self):
        pass

    def get_jira_issues(self):
        return self.jira.get_my_issues()

    def get_db_issues(self):
        return self.jira.get_my_issues()


if __name__ == "__main__":
    from envs import JIRA_USER, JIRA_TOKEN

    jira = JiraClient(JIRA_USER, JIRA_TOKEN)

    conductor = Conductor(jira)
    conductor.sync_jira_local()
