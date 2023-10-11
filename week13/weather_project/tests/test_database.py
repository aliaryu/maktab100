import unittest
from unittest.mock import MagicMock
import json

import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
from database import DataBase

class TestDataBase(unittest.TestCase):
    def setUp(self):
        self.db = DataBase(":memory:")
        with open("fixtures/city.json") as file:
            self.app = json.load(file)

    def tearDown(self):
        self.db.close_connection()

    def test_save_request_data(self):
        city = self.app[0]
        self.db.save_request_data(city)
        query = f"SELECT city_name FROM request WHERE city_name = '{city}'"
        self.db.cursor.execute(query)
        returned_data = self.db.cursor.fetchone()[0]
        self.assertEqual(city, returned_data)

    def test_save_response_data(self):
        successful = 1
        response_data = "something..."
        request_id = 1
        self.db.save_response_data(successful, response_data, request_id)
        query = f"SELECT successful, response_data, request_id FROM response"
        self.db.cursor.execute(query)
        saved_response_data = self.db.cursor.fetchall()[0]
        self.assertEqual(saved_response_data, (1, 'something...', 1))

    


if __name__ == '__main__':
    unittest.main()




