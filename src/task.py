import datetime as dt
from jira.resources import Issue as JiraIssue

from envs import JIRA_FIELD_STORY_POINTS


class BaseTask():
    """a Base Task Object"""

    def __init__(
        self,
        id: int,
        summary: str,
        project: str,
        status: str,
        description: str,
        complexity: int,
        parent: int,
        created_date: dt.datetime,
        updated_date: dt.datetime,
        due_date: dt.date,
        priority: str,
    ):
        # checks
        if status not in [None, 'To Do', 'In Progress', 'Done']:
            raise ValueError(
                f"{status} not in ['To Do','In Progress','Done']"
            )

        if priority not in [None, 'Low', 'Medium', 'High']:
            raise ValueError(
                f"{priority} not in ['Low', 'Medium', 'High']"
            )

        self.id = id
        self.summary = summary
        self.project = project
        self.status = status
        self.description = description
        self.complexity = complexity
        self.parent = parent
        self.created_date = created_date
        self.updated_date = updated_date
        self.due_date = due_date
        self.priority = priority


class DBTask(BaseTask):
    """a task object created from local database"""

    def __init__(
        self,
    ):
        super().__init__()


class JiraTask(BaseTask):
    """a task object created from a jira task"""

    def __init__(
        self,
        issue: JiraIssue,
    ):

        self.jira_id = issue.key
        summary = issue.get_field("summary")
        status = issue.get_field("status").name
        description = issue.get_field("description")
        priority = issue.get_field("priority").name

        due_date = issue.get_field("duedate")
        if due_date is not None:
            year, month, day = [
                int(value) for value in due_date.split("-")
            ]
            due_date = dt.date(year=year, month=month, day=day)

        complexity = issue.get_field(JIRA_FIELD_STORY_POINTS)
        if isinstance(complexity, float):
            complexity = int(complexity)

        super().__init__(
            id=None,
            summary=summary,
            status=status,
            project=None,
            description=description,
            complexity=complexity,
            parent=None,
            created_date=None,
            updated_date=None,
            due_date=due_date,
            priority=priority,
        )


if __name__ == "__main__":
    from jira_client import JiraClient
    from conductor import Conductor
    from envs import JIRA_USER, JIRA_TOKEN

    jira = JiraClient(JIRA_USER, JIRA_TOKEN)

    conductor = Conductor(jira)
    jira_tasks = conductor.get_issues()

    for jira_task in jira_tasks["TO DO"]:
        task = JiraTask(jira_task)
