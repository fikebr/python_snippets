import os
import sqlite3

from .config import Config

config = Config()


class Sqlite:
    def __init__(self):
        self.db_file = self.get_dbfile()
        self.db = self.dbconnect(self.db_file)

    def get_dbfile(self):
        script_folder = os.path.split(os.path.split(__file__)[0])[0]
        db_file = config.dbfile
        db_file = os.path.join(script_folder, "db", db_file)
        # print(f"dbfile: {db_file}")

        if os.path.exists(db_file):
            return db_file
        else:
            raise ("DB file not found: {}".format(db_file))

    def dbconnect(self, database_file):
        try:
            # Creates or opens a file called mydb with a SQLite3 DB
            db = sqlite3.connect(database_file)
            return db
        # Catch the exception
        except Exception as e:
            # Roll back any change if something goes wrong
            db.rollback()
            raise e

    def execute(self, sql, values=[]):
        try:
            cursor = self.db.cursor()
            # INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)
            if values:
                cursor.execute(sql, values)
            else:
                cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            # Roll back any change if something goes wrong
            self.db.rollback()
            raise e

    def select_one(self, sql):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            row = cursor.fetchone()
            return row
        except Exception as e:
            # Roll back any change if something goes wrong
            self.db.rollback()
            raise e

    def select_all(self, sql):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            print(cursor.description)
            return rows
        except Exception as e:
            # Roll back any change if something goes wrong
            self.db.rollback()
            raise e
