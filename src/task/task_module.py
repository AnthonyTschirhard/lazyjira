import datetime as dt
from jira.resources import Issue as JiraIssue

from envs import JIRA_FIELD_STORY_POINTS, JIRA_STATUS_MAP


class BaseTask():
    """a Base Task Object"""

    def __init__(
        self,
        id: int,
        jira_id: str,
        summary: str,
        project: str,
        status: str,
        description: str,
        complexity: int,
        parent: int,
        is_in_sprint: bool,
        created_date: dt.datetime,
        updated_date: dt.datetime,
        resolution_date: dt.datetime,
        due_date: dt.date,
        priority: str,
    ):
        # checks
        if status not in [
            None, 'TODO', 'IN_PROGRESS', 'DONE', 'CANCELLED',
            'READY_TO_DELIVER', "REVIEWING_REQUEST", "BACKLOG",
        ]:
            raise ValueError(
                f"{status} not in ['TODO','IN_PROGRESS','DONE', ...]"
            )

        if priority not in [None, 'LOW', 'MEDIUM', 'HIGH']:
            raise ValueError(
                f"{priority} not in ['LOW', 'MEDIUM', 'HIGH']"
            )

        self.id = id
        self.jira_id = jira_id
        self.summary = summary
        self.project = project
        self.status = status
        self.description = description
        self.complexity = complexity
        self.parent = parent
        self.is_in_sprint = is_in_sprint
        self.created_date = created_date
        self.updated_date = updated_date
        self.resolution_date = resolution_date
        self.due_date = due_date
        self.priority = priority

    def to_record(self):
        return self.__dict__


class DBTask(BaseTask):
    """a task object created from local database"""

    def __init__(
        self,
        fields: dict,
    ):
        fields["parent"] = None

        super().__init__(
            **fields
        )


class JiraTask(BaseTask):
    """a task object created from a jira task"""

    def __init__(
        self,
        issue: JiraIssue,
        active_sprint: str,
    ):

        jira_id = issue.key

        # find which tasks are in the current sprint
        sprints = issue.get_field("customfield_10007")
        if sprints is None:
            sprints = []
        is_in_sprint = any([
            sprint.name == active_sprint
            for sprint in sprints
        ])

        summary = issue.get_field("summary")
        status = JIRA_STATUS_MAP[issue.get_field("status").name]
        description = issue.get_field("description")
        priority = issue.get_field("priority").name.upper()

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
            jira_id=jira_id,
            summary=summary,
            status=status,
            project=None,
            description=description,
            complexity=complexity,
            parent=None,
            is_in_sprint=is_in_sprint,
            created_date=created_date,
            updated_date=updated_date,
            resolution_date=resolution_date,
            due_date=due_date,
            priority=priority,
        )


if __name__ == "__main__":
    from client.jira_client import JiraClient
    from client.db_client import DBClient
    from conductor import Conductor
    from envs import JIRA_USER, JIRA_TOKEN

    jira_client = JiraClient(JIRA_USER, JIRA_TOKEN)
    db_client = DBClient()

    conductor = Conductor(jira_client, db_client)

    jira_tasks = conductor.get_jira_issues()

    db_tasks = conductor.get_db_issues()
    for db_task in db_tasks:
        task = DBTask(db_task)
