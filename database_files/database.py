import sqlite3

class SQLite:
    def __init__(self, database_file):
        """_Инициализация соединения с БД"""
        self.connection = sqlite3.connect(database_file)