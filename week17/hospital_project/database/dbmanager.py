from configparser import ConfigParser, NoSectionError
import psycopg2


def config(file_name, section):
    configs = ConfigParser()
    configs.read(file_name)
    if configs.has_section(section):
        return dict(configs.items(section))
    raise NoSectionError(f"Section '{section}' not exists in '{file_name}' file")


# CONFIGS:
POSTGRES_CONFIG = config("config.ini", "postgres")
HOSPITAL_CONFIG = config("config.ini", "hospital")
QUERY_FILE_PATH = "query.sql"


class DBManager:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = psycopg2.connect(**HOSPITAL_CONFIG)
            self.cursor = self.connection.cursor()
        except:
            self._initialize()

    def _initialize(self):
        try:
            temp_connection = psycopg2.connect(**POSTGRES_CONFIG)
            temp_connection.autocommit = True
            temp_cursor = temp_connection.cursor()
            temp_cursor.execute(f"CREATE DATABASE {HOSPITAL_CONFIG['dbname']}")
        finally:
            temp_cursor.close()
            temp_connection.close()
        self.connection = psycopg2.connect(**HOSPITAL_CONFIG)
        self.cursor = self.connection.cursor()
        with open(QUERY_FILE_PATH, "r") as file:
            queries = file.read()
        self.execute_query(queries)
        self.commit_query()

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
        if self.cursor:
            self.cursor.close()
            self.cursor = None