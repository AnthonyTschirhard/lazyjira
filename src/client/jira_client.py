from envs import JIRA_USER, JIRA_TOKEN, JIRA_SERVER, GTM_OPS, JIRA_STATUS_MAP
from jira import JIRA
from jira.resources import Issue


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
        status: str = "all",
        max_results: int = 1000,
    ) -> list:
        issues = []

        all_status = JIRA_STATUS_MAP.keys()

        if status == "all":
            status_filter = list(all_status)
        elif status in all_status:
            status_filter = [status]
        else:
            raise ValueError(f"unknown status {status}")

        for status in status_filter:
            # for status in ["In progress", "To do"]:
            issues += super().search_issues(
                f"assignee=currentUser() and status='{status}'",
                maxResults=max_results,
            )

        return issues


if __name__ == "__main__":

    myjira = JiraClient(JIRA_USER, JIRA_TOKEN)

    # new_issue = myjira.create_issue(
    #     project=GTM_OPS,  # GTMP
    #     summary="Assignee TEST2",
    #     description="SUPER Long description",
    #     issue_type="Story",
    #     assignee=JIRA_USER,
    #     parent='GTMP-2317',
    #     story_points=123,
    #     version="test release"
    # )

    issues = myjira.get_my_issues()