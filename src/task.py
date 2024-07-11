import datetime as dt
from jira.resources import Issue as JiraIssue


class BaseTask():
    """a Base Task Object"""

    def __init__(
        self,
        id: int,
        name: str,
        project: str,
        status: str,
        jira_id: str,
        description: str,
        complexity: int,
        parent: int,
        created_date: dt.datetime,
        updated_date: dt.datetime,
        due_date: dt.datetime,
        priority: str,
    ):
        # checks
        if status not in [None, 'ToDo', 'InProgress', 'Done']:
            raise ValueError(
                f"{status} not in ['ToDo','InProgress','Done']"
            )

        if priority not in [None, 'Low', 'Medium', 'High']:
            raise ValueError(
                f"{priority} not in ['Low', 'Medium', 'High']"
            )

        self.id = id
        self.name = name
        self.project = project
        self.status = status
        self.jira_id = jira_id
        self.description = description
        self.complexity = complexity
        self.parent = parent
        self.created_date = created_date
        self.updated_date = updated_date
        self.due_date = due_date
        self.priority = priority


class DBTask(BaseTask):
    """a task object created from local databse"""

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

        jira_id = issue.get_field("key")
        name = issue.get_field("name")
        status = issue.get_field("status")
        # project =
        # description =
        # complexity =
        # parent =
        # created_date =
        # updated_date =
        # due_date =
        # priority =

        super().__init__(
            id=None,
            name=name,
            project=None,
            status=status,
            jira_id=jira_id,
            description=None,
            complexity=None,
            parent=None,
            created_date=None,
            updated_date=None,
            due_date=None,
            priority=None,
        )


if __name__ == "__main__":
    pass
