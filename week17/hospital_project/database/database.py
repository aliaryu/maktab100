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

    @staticmethod
    def doctor_visits_info():
        with DBManager() as db:
            query = """SELECT fullname, specialization, COUNT(visit_id) AS number_of_visits, SUM(cost)
            AS income FROM users u JOIN doctors d ON u.user_id = d.user_id JOIN appointments a ON
            d.doctor_id = a.doctor_id JOIN visits v ON a.appointment_id = v.appointment_id WHERE
            paid = true GROUP BY fullname, specialization;"""
            db.execute_query(query)
            return db.fetch_all()
    
    @staticmethod
    def income_daily():
        with DBManager() as db:
            query = """SELECT SUM(cost) AS income_daily FROM visits v JOIN appointments a ON
            v.appointment_id = a.appointment_id WHERE v.paid_date = CURRENT_DATE AND
            v.paid = TRUE;"""
            db.execute_query(query)
            return db.fetch_one()[0]
    
    @staticmethod
    def income_weekly():
        with DBManager() as db:
            query = """SELECT SUM(cost) AS income_weekly FROM visits v JOIN appointments a ON
            v.appointment_id = a.appointment_id WHERE v.paid_date >= NOW() - INTERVAL '1 week'
            AND v.paid_date < NOW() AND v.paid = TRUE;"""
            db.execute_query(query)
            return db.fetch_one()[0]
        
    @staticmethod
    def income_monthly():
        with DBManager() as db:
            query = """SELECT SUM(cost) AS income_monthly FROM visits v JOIN appointments a ON
            v.appointment_id = a.appointment_id WHERE v.paid_date >= NOW() - INTERVAL '1 month'
            AND v.paid_date < NOW() AND v.paid = TRUE;"""
            db.execute_query(query)
            return db.fetch_one()[0]
        



    


# # Admin.list_patients
# result = Admin.list_patients()
# print("fullname".ljust(20), "date_of_birth".ljust(15), "gender".ljust(8), "medical_record_number".ljust(10), "\n")
# for item in result:
#     print(item[0].ljust(20), item[1].strftime("%Y-%m-%d").ljust(15), item[2].ljust(8), str(item[3]).ljust(10))

# # Admin.list_doctors
# result = Admin.list_doctors()
# print("fullname".ljust(20), "date_of_birth".ljust(15), "gender".ljust(8), "specialization".ljust(20), "medical_license_number".ljust(20), "\n")
# for item in result:
#     print(item[0].ljust(20), item[1].strftime("%Y-%m-%d").ljust(15), item[2].ljust(8), item[3].ljust(20), str(item[4]).ljust(20))

# # Admin.doctor_visits_info
# result = Admin.doctor_visits_info()
# print("fullname".ljust(20), "specialization".ljust(20), "number_of_visits".ljust(20), "income".ljust(10), "\n")
# for item in result:
#     print(item[0].ljust(20), item[1].ljust(20), str(item[2]).ljust(20), str(float(item[3])).ljust(10))

# # Admin.income_daily
# result = Admin.income_daily()
# print(f"Daily Income: {result}")

# # Admin.income_weekly
# result = Admin.income_weekly()
# print(f"Weekly Income: {result}")

# # Admin.income_monthly
# result = Admin.income_monthly()
# print(f"Weekly Income: {result}")