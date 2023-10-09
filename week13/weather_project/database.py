import sqlite3
import datetime
from typing import List, Tuple


class DataBase():
    def __init__(self, path="."):
        self.connection = sqlite3.connect(f"{path}/database.db")
        self.cursor = self.connection.cursor()
        self.create_table()
    
    def create_table(self) -> None:
        """
        This function creates database with two table:
            1 - Table request
            2 - Table response
        Returns: None
        """
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

    def save_request_data(self, city_name:str) -> int:
        """
        Save request data for a city to the database.
        Args:
            - city_name (str): The name of the city to save request data for.
        Returns: int, the last row id, for save in response we need request id.
        """
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = f"""
            INSERT INTO request (city_name, request_time) 
            VALUES ('{city_name}', '{now}')
        """
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.lastrowid
    
    def save_response_data(self, successful: int, response_data: str, request_id: int) -> None:
        """
        Save response data to the database.
        Args:
            - successful (int): Whether the response was successful (1) or not (0).
            - response_data (str): The response data to save.
            - request_id (int): The id of the associated request.
        Returns: None
        """
        query = f"""
            INSERT INTO response (successful, response_data, request_id)
            VALUES ('{successful}', '{response_data}', '{request_id}')
        """
        self.cursor.execute(query)
        self.connection.commit()

    def get_request_count(self) -> int:
        """
        Get the total number of requests made to the server.
        Returns: int, total number of requests made to the server.
        """
        query = "SELECT COUNT(*) FROM request"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
    
    def get_successful_request_count(self) -> int:
        """
        Get the total number of successful requests made to the server.
        Returns: int, total number of successful requests made to the server.
        """
        query = "SELECT COUNT(*) FROM response WHERE successful = 1"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def get_last_hour_requests(self) -> List[List]:
        """
        Get all requests made in the last hour.
        Returns: list, A list of lists containing
        the request city name, and request time.
        """
        hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1)
        query = f"SELECT city_name, request_time FROM request WHERE request_time >= '{hour_ago}'"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_count_requests_by_city(self) -> List[List]:
        """
        Count the number of requests for each city.
        Returns: list, A list of lists where each tuple contains
        the city name and the corresponding request count.
        """
        query = "SELECT city_name, COUNT(*) FROM request GROUP BY city_name"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self) -> None:
        """
        Close connection. Easy.
        """
        self.connection.close()
