import datetime as dt
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import select, insert, update

from task import JiraTask

from envs import SQLITE_PATH, TASK_TABLE, WORK_TABLE, STD_TIME_FORMAT


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

        self.workhour_table = Table(
            WORK_TABLE,
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

    def get_active_task(self) -> int:
        """returns the id of the current active task in the database"""
        select_stmt = select(self.workhour_table).where(
            self.workhour_table.c.end_time.is_(None)
        )
        with self.engine.connect() as con:
            result = con.execute(select_stmt).all()

        if len(result) == 0:
            return None
        elif len(result) == 1:
            return int(result[0]._asdict()["task"])
        else:
            ids = [r._asdict()["task"] for r in result]
            raise ValueError(
                f"More than one active task: {ids}"
            )

    def start_stop_task(
        self,
        task_id: int,
    ):
        active_task = self.get_active_task()

        now = dt.datetime.now()

        # stop the current active task
        if task_id == active_task:
            update_stmt = update(
                self.workhour_table
            ).where(
                self.workhour_table.c.end_time.is_(None)
            ).values(
                {
                    "end_time": now
                }
            )
            with self.engine.connect() as con:
                con.execute(update_stmt)
                con.commit()

        # start the task task_id
        elif active_task is None:
            insert_stmt = insert(
                self.workhour_table
            ).values(
                {
                    "task": task_id,
                    "start_time": now,
                    "end_time": None,
                }
            )
            with self.engine.connect() as con:
                con.execute(insert_stmt)
                con.commit()

        # else raise a ValueError
        else:
            raise ValueError((
                f"task {task_id} can't be started while"
                f"{active_task} is running"
            ))


if __name__ == "__main__":
    client = DBClient()
    print(client.get_active_task())
    client.start_stop_task(1)
    client.start_stop_task(2)
