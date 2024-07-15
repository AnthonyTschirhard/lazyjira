from task import JiraTask
from jira_client import JiraClient
from textual.widgets import Static


class Conductor():

    def __init__(
        self,
        jira: JiraClient,
    ):
        self.jira = jira

    def sync_jira_local(self):
        issues = self.jira.get_my_issues()
        for issue in issues["IN PROGRESS"]:
            jira_task = JiraTask(issue)

    # TODO: just for tests
    def get_issues(self):
        issues = self.jira.get_my_issues()
        return_ = [
            JiraTask(issue).summary
            for issue in issues["IN PROGRESS"] + issues["TO DO"]
        ]

        return return_


if __name__ == "__main__":
    from envs import JIRA_USER, JIRA_TOKEN

    jira = JiraClient(JIRA_USER, JIRA_TOKEN)

    conductor = Conductor(jira)
    conductor.sync_jira_local()
