import sqlite3

# Use SQLite
# https://docs.python.org/3.8/library/sqlite3.html


class DBConnection(object):
    """docstring for DBConnection.

        Current implementation is only for SQLite databases
    """

    def __init__(self, database):
        super(DBConnection, self).__init__()
        self.database = database
        self.connection = None
        self.cursor = None

    """
        Connect to database and create cursor
    """
    def connect(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    """
        Disconnect discarding changes
    """
    def disconnect(self):
        self.connection.close()

    """
        Disconnect saving changes
    """
    def close(self):
        self.save_changes()
        self.disconnect()

    """
        Commit changes to database
    """
    def save_changes(self):
        self.connection.commit()

    """
        Run sql command on database
    """
    def excecute_sql(self, sql):
        self.cursor.excecute(sql)

    """
        Run sql and commit changes
    """
    def excecute_save(self, sql):
        self.excecute_sql(sql)
        self.save_changes()
