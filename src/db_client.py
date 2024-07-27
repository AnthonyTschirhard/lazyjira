from sqlalchemy import create_engine, MetaData, Table, select

from envs import SQLITE_PATH, TASK_TABLE


class DBClient():
    """SQLite Client"""

    def __init__(self):
        self.engine = create_engine(f"sqlite:////{SQLITE_PATH}")
        self.metadata = MetaData()

    def create_task(
        self,
    ) -> None:
        """creates an issue in the local database"""
        pass

    def update_task(
        self,
    ):
        pass

    def get_tasks(self):
        task_table = Table(
            TASK_TABLE,
            self.metadata,
            autoload_with=self.engine
        )
        stmt = select(task_table)
        with self.engine.connect() as con:
            rows = con.execute(stmt).all()

        return [
            row._asdict()
            for row in rows
        ]


if __name__ == "__main__":
    client = DBClient()
    client.get_tasks()
