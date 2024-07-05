import datetime as dt
from sqlalchemy import create_engine

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class SQLClient():

    def __init__(
        self,
        db_file: str,
    ):
        self.engine = create_engine(f"sqlite:///{db_file}")

    def get_total_time(
        self,
        task_name: str,
    ) -> float:
        """get the total number of hours spent on task_name"""

        total_duration = 0

        with self.engine.connect() as conn:
            results = conn.exec_driver_sql((
                "SELECT start_time, end_time "
                "FROM work_hours "
                f"WHERE issue = '{task_name}'"
            ))
            for row in results:
                start_time = dt.datetime.strptime(row[0], DATETIME_FORMAT)
                end_time = dt.datetime.strptime(row[1], DATETIME_FORMAT)

                duration = (end_time - start_time).total_seconds()
                total_duration += duration

        return total_duration/3600

    def has_project(
        self,
        task_name: str,
    ) -> float:
        """has task_name a project in the database"""

        with self.engine.connect() as conn:
            results = conn.exec_driver_sql((
                "SELECT project "
                "FROM tasks "
                f"WHERE name = '{task_name}'"
            )).all()

        return bool(results)

    def set_project(
        self,
        task_name: str,
        project_name: str,
    ) -> None:
        """set task_name the project project_name"""

        with self.engine.connect() as conn:
            conn.exec_driver_sql((
                "UPDATE tasks "
                f"SET project = '{project_name}' "
                f"WHERE name = '{task_name}'"
            ))
            conn.commit()


if __name__ == "__main__":
    client = SQLClient("/home/atschirhard/Sources/lazyjira/brother.db")
    print(client.get_total_time("GTMP-1") == 16.0)
    print(client.has_project("GTMP-1"))
    print(client.has_project("GTMP-4") == False)
    client.set_project("GTMP-3", "Project D")
    input("end")
