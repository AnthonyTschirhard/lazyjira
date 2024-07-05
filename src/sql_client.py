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


if __name__ == "__main__":
    client = SQLClient("/home/atschirhard/Sources/lazyjira/brother.db")
    print(client.get_total_time("GTMP-1") == 16.0)
    print(client.has_project("GTMP-1"))
    input("end")
