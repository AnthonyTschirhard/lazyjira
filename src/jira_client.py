from jira import JIRA
from jira.resources import Issue


JIRA_SERVER = "https://bic-americas.atlassian.net/"
ME = '712020:a61ed3d4-7c90-4665-b6fc-09cb0c7c69be'
GTM_OPS = 12401


class JiraClient(JIRA):
    """a Jira Client"""

    def __init__(
        self,
        user: str,
        token: str,
    ):
        super().__init__(
            server=JIRA_SERVER,
            basic_auth=(user, token),
        )

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
    ) -> Issue:
        """creates an issue in Jira"""
        parent_issue = self.issue(parent)
        issue_dict = {
            "project": {"id": project},
            "summary": summary,
            "description": description,
            "issuetype": {"name": issue_type},
            "assignee": assignee,
            "parent": {
                "key": parent_issue.key
            },
        }
        new_issue = super().create_issue(fields=issue_dict)

        if (
            story_points is not None
            and version is not None
        ):
            self.update_issue(
                new_issue.key,
                story_points=story_points,
                version=version
            )

        return new_issue

    def update_issue(
        self,
        issue_name: str,
        story_points: int = None,
        version: str = None,
    ):
        issue = self.issue(issue_name)
        fields = {}

        if story_points is not None:
            fields["customfield_10005"] = story_points

        if version is not None:
            fields["fixVersions"] = [
                {
                    "set": [{
                        "name": version
                    }]
                }
            ]

        update = issue.update(fields=fields)

        return update

    def get_my_issues(
        self,
    ) -> list[Issue]:
        issues = super().search_issues(f"assignee=currentUser()")
        return issues


if __name__ == "__main__":
    import os

    jira_user = os.environ['JIRA_USER']
    jira_token = os.environ['JIRA_API_TOKEN']
    myjira = JiraClient(jira_user, jira_token)

    new_issue = myjira.create_issue(
        project=GTM_OPS,  # GTMP
        summary="Assignee TEST2",
        description="SUPER Long description",
        issue_type="Story",
        assignee=jira_user,
        parent='GTMP-2317',
        story_points=123,
        version="test release"
    )

    issues = myjira.get_my_issues()
    x = 0
