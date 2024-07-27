from client.jira_client import JiraClient
from client.db_client import DBClient

from task.task import JiraTask, DBTask


class Conductor():

    def __init__(
        self,
        jira_client: JiraClient,
        db_client: DBClient,
    ):
        self.jira_client = jira_client
        self.db_client = db_client

    def get_jira_issues(self):
        return [
            JiraTask(task)
            for task in self.jira_client.get_my_issues()
        ]

    def get_db_issues(self):
        return [
            DBTask(task)
            for task in self.db_client.get_tasks()
        ]

    def sync_jira_local(self):
        jira_tasks = self.get_jira_issues()
        db_tasks = self.get_db_issues()

        jira_ids_mapping = {
            task.jira_id: task
            for task in db_tasks
            if task.jira_id is not None
        }

        for jira_task in jira_tasks:
            if jira_task.jira_id in jira_ids_mapping:
                jira_task.id = jira_ids_mapping[jira_task.jira_id].id
                self.update_local_task(jira_task)
            else:
                self.create_local_task(jira_task)

    def update_local_task(
        self,
        jira_task: JiraTask,
    ):
        self.db_client.update_task(jira_task)

    def create_local_task(
        self,
        jira_task: JiraTask,
    ):
        self.db_client.create_task(jira_task)


if __name__ == "__main__":
    from envs import JIRA_USER, JIRA_TOKEN

    jira_client = JiraClient(JIRA_USER, JIRA_TOKEN)
    db_client = DBClient()

    conductor = Conductor(jira_client, db_client)
    conductor.sync_jira_local()
