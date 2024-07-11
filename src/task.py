import datetime as dt


class Task():
    """a Task Object"""

    def __init__(
        self,
        id: int,
        name: str,
        project: str,
        status: str,
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
        self.description = description
        self.complexity = complexity
        self.parent = parent
        self.created_date = created_date
        self.updated_date = updated_date
        self.due_date = due_date
        self.priority = priority


if __name__ == "__main__":
    pass
