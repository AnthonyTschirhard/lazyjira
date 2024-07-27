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
        resolution_date: dt.datetime,
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
        self.resolution_date = resolution_date
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

        created_date = dt.datetime.fromisoformat(issue.get_field("created"))
        updated_date = dt.datetime.fromisoformat(issue.get_field("updated"))
        resolution_date = issue.get_field("resolutiondate")
        if resolution_date is not None:
            resolution_date = dt.datetime.fromisoformat(resolution_date)

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
            created_date=created_date,
            updated_date=updated_date,
            resolution_date=resolution_date,
            due_date=due_date,
            priority=priority,
        )


if __name__ == "__main__":
    from jira_client import JiraClient
    from db_client import DBClient
    from conductor import Conductor
    from envs import JIRA_USER, JIRA_TOKEN

    jira_client = JiraClient(JIRA_USER, JIRA_TOKEN)
    db_client = DBClient()

    conductor = Conductor(jira_client, db_client)
    jira_tasks = conductor.get_jira_issues()

    for jira_task in jira_tasks["DONE"]:
        task = JiraTask(jira_task)
