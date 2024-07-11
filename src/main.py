import os
from jira_client import JiraClient
from sql_client import SQLClient

from jira_client import GTM_OPS

DB_PATH = "/home/atschirhard/Sources/lazyjira/brother.db"

if __name__ == "__main__":

    # Initialize objects
    jira_user = os.environ['JIRA_USER']
    jira_token = os.environ['JIRA_API_TOKEN']
    jira_client = JiraClient(jira_user, jira_token)
    sql_client = SQLClient(DB_PATH)

    # new_issue = jira_client.create_issue(
    #     project=GTM_OPS,  # GTMP
    #     summary="Super TEST",
    #     description="SUPER Long description",
    #     issue_type="Story",
    #     assignee=jira_user,
    #     parent='GTMP-2317',
    #     story_points=123,
    #     version="test release"
    # )

    # Get Jira issues
    issues = jira_client.get_my_issues()

    for issue in issues:
        print(
            f"{issue.key}: {issue.fields.issuetype.name}"
        )
        if issue.fields.issuetype.name == "Task":
            print(f"    {issue.fields.issuetype.description}")

    input("end")
