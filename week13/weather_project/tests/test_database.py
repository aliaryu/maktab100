import unittest
from datetime import datetime, timedelta
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

    def test_get_request_count(self):
        for city in self.app:
            self.db.save_request_data(city)
        request_count = self.db.get_request_count()
        self.assertEqual(request_count, len(self.app))

    def test_get_successful_request_count(self):
        self.db.save_response_data(1, "something...", 1)
        self.db.save_response_data(1, "something...", 2)
        self.db.save_response_data(0, "error message", 3)
        successful_request_count = self.db.get_successful_request_count()
        self.assertEqual(successful_request_count, 2)

    def test_get_last_hour_requests(self):
        now = datetime.now()
        two_hours_ago = now - timedelta(hours=2)
        self.db.save_request_data("london")
        self.db.save_request_data("paris")
        self.db.save_request_data("new York")
        query = f"UPDATE request SET request_time = '{two_hours_ago}' WHERE id = 3"
        self.db.cursor.execute(query)
        last_hour_requests = self.db.get_last_hour_requests()
        self.assertEqual([item[0] for item in last_hour_requests], ["london", "paris"])

    def test_get_count_requests_by_city(self):
        self.db.save_request_data("london")
        self.db.save_request_data("paris")
        self.db.save_request_data("tehran")
        self.db.save_request_data("london")
        self.db.save_request_data("paris")
        count_requests_by_city = self.db.get_count_requests_by_city()
        self.assertEqual(count_requests_by_city, [("london", 2), ("paris", 2), ("tehran", 1)])
        

if __name__ == '__main__':
    unittest.main()




