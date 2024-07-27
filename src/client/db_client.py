from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import select, insert, update

from task.task import JiraTask

from envs import SQLITE_PATH, TASK_TABLE


class DBClient():
    """SQLite Client"""

    def __init__(self):
        self.engine = create_engine(f"sqlite:////{SQLITE_PATH}")
        self.metadata = MetaData()

        self.task_table = Table(
            TASK_TABLE,
            self.metadata,
            autoload_with=self.engine
        )

    def get_tasks(self):
        stmt = select(self.task_table)
        with self.engine.connect() as con:
            rows = con.execute(stmt).all()

        return [
            row._asdict()
            for row in rows
        ]

    def update_task(
        self,
        task: JiraTask,
    ) -> None:
        update_stmt = update(self.task_table)

        with self.engine.connect() as con:
            record = task.to_record()
            con.execute(update_stmt, task.to_record())
            con.commit()


if __name__ == "__main__":
    client = DBClient()
    client.get_tasks()
