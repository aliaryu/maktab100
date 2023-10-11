import unittest
from unittest.mock import MagicMock
import json

import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
from weather_server import get_city_weather
from database import DataBase

class TestGetCityWeather(unittest.TestCase):
    def setUp(self):
        with open("fixtures/city.json") as file:
            self.app = json.load(file)

    def test_get_city_weather_success(self):
        db = MagicMock(DataBase)
        db.save_request_data.return_value = 1
        db.save_response_data.return_value = None

        with unittest.mock.patch("weather_server.DataBase", db):
            for city in self.app:
                response = get_city_weather(city_name=city)
                self.assertIn("temperature", response)
                self.assertIn("last_updated", response)
                self.assertIn("feels_like", response)

    def test_notfound_city_weather(self):
        db = MagicMock(DataBase)
        db.save_request_data.return_value = 1
        db.save_response_data.return_value = None

        with unittest.mock.patch("weather_server.DataBase", db):
            city = "notfound"
            response = get_city_weather(city_name=city)
            self.assertEqual("No matching location found.", response)


if __name__ == '__main__':
    unittest.main()