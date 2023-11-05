from configparser import ConfigParser, NoSectionError


def config(file_name, section):
    configs = ConfigParser()
    configs.read(file_name)
    if configs.has_section(section):
        return dict(configs.items(section))
    raise NoSectionError(f"Section '{section}' not exists in '{file_name}' file")


class DBManager:
    def __init__(self):
        self.connection = None
        self.cursor = None
