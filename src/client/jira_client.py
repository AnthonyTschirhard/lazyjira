import datetime as dt

from envs import BOARD_ID
from envs import JIRA_USER, JIRA_TOKEN, JIRA_SERVER
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
        max_results: int = 100,
        cutoff_date: dt.datetime = None
    ) -> list:
        index_ = 0
        all_issues = []

        request = "assignee=currentUser()"

        if cutoff_date:
            cutoff_str = cutoff_date.strftime("%Y-%m-%d %H:%M")
            request += f"AND updated > '{cutoff_str}'"

        while True:
            issues = super().search_issues(
                request,
                maxResults=max_results,
                startAt=index_,
            )
            if issues:
                index_ += len(issues)
                all_issues = all_issues + issues
            else:
                return all_issues

    def get_active_sprint(self) -> str:
        """return the name of the active sprint"""
        index_ = 0
        last_sprint = None

        while True:
            sprints = super().sprints(
                board_id=BOARD_ID,
                startAt=index_,
            )
            if sprints:
                last_sprint = sprints[-1]
                index_ += len(sprints)
            else:
                return last_sprint.name


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

    # print(myjira.get_active_sprint())
