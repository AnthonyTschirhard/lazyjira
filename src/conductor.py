from envs import JIRA_USER, JIRA_TOKEN
from task import Task
from jira_client import JiraClient


class Conductor():

    def __init__(
        self,
        jira: JiraClient,
    ):
        self.jira = jira

    def sync_jira_local(self):
        issues = self.jira.get_my_issues()


if __name__ == "__main__":
    jira = JiraClient(JIRA_USER, JIRA_TOKEN)

    conductor = Conductor(jira)
