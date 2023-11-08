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

# LOGGER DOCTOR
logger_doctor = logging.getLogger("database.Doctor")
file_handler_doctor = logging.FileHandler(OUTPUT_FOLDER + "doctor.log")
file_handler_doctor.setFormatter(HANDLER_FORMAT)
file_handler_doctor.setLevel(logging.INFO)
logger_doctor.addHandler(file_handler_doctor)
logger_doctor.setLevel(logging.INFO)

# LOGGER PATIENT
logger_patient = logging.getLogger("database.Patient")
file_handler_patient = logging.FileHandler(OUTPUT_FOLDER + "patient.log")
file_handler_patient.setFormatter(HANDLER_FORMAT)
file_handler_patient.setLevel(logging.INFO)
logger_patient.addHandler(file_handler_patient)
logger_patient.setLevel(logging.INFO)
