from configparser import ConfigParser, NoSectionError


def config(file_name, section):
    configs = ConfigParser()
    configs.read(file_name)
    if configs.has_section(section):
        return dict(configs.items(section))
    raise NoSectionError(f"Section '{section}' not exists in '{file_name}' file")


# CONFIGS:
POSTGRES_CONFIG = config("config.ini", "postgres")
HOSPITAL_CONFIG = config("config.ini", "hospital")


class DBManager:
    def __init__(self):
        self.connection = None
        self.cursor = None
