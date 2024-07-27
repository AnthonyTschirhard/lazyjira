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
        table = self.task_table
        primary_key_columns = table.primary_key.columns

        record = task.to_record()

        where_stmt = None
        for key in primary_key_columns:
            if where_stmt is None:
                where_stmt = (
                    table.columns[key.name] == record[key.name]
                )
            else:
                where_stmt &= (
                    table.columns[key.name] == record[key.name]
                )
            record.pop(key.name)

        update_stmt = update(table).where(where_stmt).values(record)

        with self.engine.connect() as con:
            con.execute(update_stmt)
            con.commit()

    def create_task(
        self,
        task: JiraTask,
    ) -> None:
        insert_stmt = insert(self.task_table)

        with self.engine.connect() as con:
            con.execute(insert_stmt, task.to_record())
            con.commit()


if __name__ == "__main__":
    client = DBClient()
    client.get_tasks()
