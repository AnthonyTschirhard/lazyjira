from envs import SQLITE_PATH


class DBClient():
    """SQLite Client"""

    def create_issue(
        self,
        project: int,
        summary: str,
        description: str,
        issue_type: str,
        assignee: str,
        parent: str,
        story_points: int = None,
        version: str = None,
    ) -> None:
        """creates an issue in the local database"""
        pass

    def update_issue(
        self,
    ):
        pass


if __name__ == "__main__":
    pass
