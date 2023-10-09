import sqlite3


class DataBase():
    def __init__(self, path="."):
        self.connection = sqlite3.connect(f"{path}/database.db")
        self.cursor = self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        query_table_request = """
            CREATE TABLE IF NOT EXISTS
            request(
                id INTEGER PRIMARY KEY,
                city_name TEXT NOT NULL,
                request_time TEXT NOT NULL
            )
        """
        query_table_response = """
            CREATE TABLE IF NOT EXISTS
            response(
                id INTEGER PRIMARY KEY,
                successful INTEGER NOT NULL,
                response_data TEXT NOT NULL,
                request_id INTEGER UNIQUE,
                FOREIGN KEY (request_id) REFERENCES request(id)
            )
        """
        self.cursor.execute(query_table_request)
        self.cursor.execute(query_table_response)


a = DataBase()