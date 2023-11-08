import sys
from pathlib import Path
project_folder = Path(__file__).resolve().parent.parent
sys.path.append(str(project_folder))

import unittest
from unittest.mock import patch
from database.dbmanager import DBManager, config

class TestDBManager(unittest.TestCase):
    def setUp(self):
        with patch('database.dbmanager.HOSPITAL_CONFIG', config("database/config.ini", "test_hospital")):
            self.db = DBManager()
    
    def tearDown(self) -> None:
        self.db.close()

    def test_fetch_one(self):
        self.db.execute_query("SELECT user_id FROM users WHERE user_id = 1;")
        result = self.db.fetch_one()
        expected = (1,)
        self.assertEqual(result, expected)
    
    def test_fetch_all(self):
        self.db.execute_query("SELECT user_id FROM users ORDER BY user_id LIMIT 3;")
        result = self.db.fetch_all()
        expected = [(1,), (2,), (3,)]
        self.assertEqual(result, expected)

    def test_commit_query(self):
        self.db.execute_query("UPDATE users SET delete = TRUE WHERE user_id = 1 RETURNING user_id;")
        result = self.db.fetch_one()
        expected = (1,)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
