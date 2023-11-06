from dbmanager import DBManager

from datetime import datetime


class Admin:

    @staticmethod
    def list_patients():
        with DBManager() as db:
            query = """SELECT fullname, date_of_birth, gender, medical_record_number
            FROM users u JOIN patients p ON u.user_id = p.user_id LIMIT 50;"""
            db.execute_query(query)
            return db.fetch_all()
        
    @staticmethod
    def list_doctors():
        with DBManager() as db:
            query = """SELECT fullname, date_of_birth, gender, specialization, medical_license_number
            FROM users u JOIN doctors d ON u.user_id = d.user_id LIMIT 50;"""
            db.execute_query(query)
            return db.fetch_all()








# # Admin.list_patients
# result = Admin.list_patients()
# print("fullname".ljust(20), "date_of_birth".ljust(15), "gender".ljust(8), "medical_record_number".ljust(10), "\n")
# for item in result:
#     print(item[0].ljust(20), item[1].strftime("%Y-%m-%d").ljust(15), item[2].ljust(8), str(item[3]).ljust(10))

# # Admin.list_doctors
# result = Admin.list_doctors()
# print("fullname".ljust(20), "date_of_birth".ljust(15), "gender".ljust(8), "specialization".ljust(20), "medical_license_number".ljust(15), "\n")
# for item in result:
#     print(item[0].ljust(20), item[1].strftime("%Y-%m-%d").ljust(15), item[2].ljust(8), item[3].ljust(20), str(item[4]).ljust(15))