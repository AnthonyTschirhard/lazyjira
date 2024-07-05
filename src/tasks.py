import os

from jira.resources import Issue

from jira_client import JiraClient


class TaskFileNotFoundError(FileNotFoundError):
    pass


class Task(Issue):
    """Various tasks"""

    def __init__(
        self,
        jira_issue: Issue,
        log_folder: str,
    ):
        self.duration: float

        # check if log file exists
        file_path = os.path.join(log_folder, jira_issue.key + ".json")
        self._check_log_file(file_path)

        self.__dict__ = jira_issue.__dict__

    def _check_log_file(
        self,
        file_path: str,
    ):
        if not os.path.exists(file_path):
            raise TaskFileNotFoundError(f"File {file_path} not found")


if __name__ == "__main__":
    import os

    jira_user = os.environ['JIRA_USER']
    jira_token = os.environ['JIRA_API_TOKEN']

    myjira = JiraClient(jira_user, jira_token)
    jira_task = myjira.issue("GTMP-5927")

    my_task = Task(
        jira_task,
        "data"
    )
