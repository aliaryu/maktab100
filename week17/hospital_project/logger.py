import logging

# CONFIGS
OUTPUT_FOLDER  = "logs/"
HANDLER_FORMAT = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s")

# LOGGER USER
logger_user = logging.getLogger("database.User")
file_handler_user = logging.FileHandler(OUTPUT_FOLDER + "user.log")
file_handler_user.setFormatter(HANDLER_FORMAT)
file_handler_user.setLevel(logging.INFO)
logger_user.addHandler(file_handler_user)
logger_user.setLevel(logging.INFO)








