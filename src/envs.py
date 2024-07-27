import os

JIRA_USER = os.environ['JIRA_USER']
JIRA_TOKEN = os.environ['JIRA_API_TOKEN']
JIRA_SERVER = "https://bic-americas.atlassian.net/"
JIRA_FIELD_STORY_POINTS = "customfield_10005"
JIRA_STATUS_MAP = {
    "To Do": "TODO",
    "In Progrss": "IN_PROGRESS",
    "Done": "DONE",
}
GTM_OPS = 12401

SQLITE_PATH = "/home/atschirhard/Sources/lazyjira/brother.db"

TASK_TABLE = "task"
