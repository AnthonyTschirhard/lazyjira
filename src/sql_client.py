import os
from sqlalchemy import create_engine


class SQLClient():

    def __init__(
        self,
        db_file: str,
    ):
        self.engine = create_engine(f"sqlite:////{db_file}")
        self.engine.connect()


if __name__ == "__main__":
    client = SQLClient("brother.db")
