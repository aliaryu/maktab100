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

    def test_insert(self):
        pass



if __name__ == '__main__':
    unittest.main()
