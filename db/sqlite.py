import os
import sqlite3
from typing import Union, List, Optional


class SQLite:
    def __init__(self, db_filename: str) -> None:
        self.db_file = self.get_dbfile(db_filename)
        self.db = self.dbconnect(self.db_file)

    def get_dbfile(self, filename: str) -> str:
        if os.path.exists(filename):
            return filename

        script_folder = os.path.dirname(os.path.abspath(__file__))
        db_file = os.path.join(script_folder, "db", filename)
        # print(f"Database file: {db_file}")

        if not os.path.exists(db_file):
            raise FileNotFoundError(f"Database file not found: {db_file}")

        return db_file

    def dbconnect(self, database_file: str) -> sqlite3.Connection:
        try:
            # Creates or opens a file called mydb with a SQLite3 DB
            db = sqlite3.connect(database_file)
            return db
        except Exception as e:
            print(f"Error connecting to database: {e}")
            raise

    def execute(self, sql: str, values: Union[List[any], tuple] = []) -> int:
        try:
            with self.db:
                cursor = self.db.cursor()
                cursor.execute(sql, values)
                return cursor.rowcount
        except Exception as e:
            print(f"Error executing SQL: {e}")
            raise

    def select_one(self, sql: str) -> Optional[tuple]:
        try:
            with self.db:
                cursor = self.db.cursor()
                cursor.execute(sql)
                return cursor.fetchone()
        except Exception as e:
            print(f"Error executing SELECT query: {e}")
            raise

    def select_all(self, sql: str) -> List[tuple]:
        try:
            with self.db:
                cursor = self.db.cursor()
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(f"Error executing SELECT query: {e}")
            raise
