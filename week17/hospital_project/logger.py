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

# LOGGER ADMIN
logger_admin = logging.getLogger("database.Admin")
file_handler_admin = logging.FileHandler(OUTPUT_FOLDER + "admin.log")
file_handler_admin.setFormatter(HANDLER_FORMAT)
file_handler_admin.setLevel(logging.INFO)
logger_admin.addHandler(file_handler_admin)
logger_admin.setLevel(logging.INFO)




# logger_user.info("info")
# logger_admin.info("admin")

