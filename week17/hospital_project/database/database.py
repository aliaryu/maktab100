from .dbmanager import DBManager
import bcrypt


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), b'$2b$12$0KdMmFngvGhqBI0CMM/Lp.')


class User:

    @staticmethod
    def sign_in(username, password):
        with DBManager() as db:
            query = """SELECT * FROM users WHERE username = %s"""
            db.execute_query(query, (username,))
            result = db.fetch_one()
            if result:
                if bcrypt.checkpw(password.encode("utf-8"), bytes(result[6])):
                    return result

    @staticmethod
    def sign_up_doctor(fullname, email, date_of_birth, gender, username, password,
                       specialization, medical_license_number):
        password = hash_password(password)
        with DBManager() as db:
            query_users = """INSERT INTO users (fullname, email, date_of_birth, gender,
            username, password, role) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING user_id"""
            query_doctors = """INSERT INTO doctors (user_id, specialization, medical_license_number)
            VALUES (%s, %s, %s)"""
            db.execute_query(query_users, (fullname, email, date_of_birth, gender, username,
                                            password, "doctor"))
            db.execute_query(query_doctors, (db.fetch_one()[0], specialization, medical_license_number))
            db.commit_query()

    @staticmethod
    def sign_up_patient(fullname, email, date_of_birth, gender, username, password,
                        medical_record_number):
        password = hash_password(password)
        with DBManager() as db:
            query_users = """INSERT INTO users (fullname, email, date_of_birth, gender,
            username, password, role) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING user_id"""
            query_patients = """INSERT INTO patients (user_id, medical_record_number)
            VALUES (%s, %s)"""
            db.execute_query(query_users, (fullname, email, date_of_birth, gender, username,
                                            password, "patient"))
            db.execute_query(query_patients, (db.fetch_one()[0], medical_record_number))
            db.commit_query()


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
    def visits_info():
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
    
    @staticmethod
    def show_inactive_users():
        with DBManager() as db:
            query = """SELECT user_id, fullname, email, date_of_birth, gender, username, role,
            superuser, active, delete FROM users WHERE active = FALSE AND delete = FALSE LIMIT 10;"""
            db.execute_query(query)
            return db.fetch_all()
        
    @staticmethod
    def active_user(user_id):
        with DBManager() as db:
            query = """UPDATE users SET active = TRUE, delete = FALSE WHERE user_id = %s"""
            db.execute_query(query, (user_id,))
            db.commit_query()

    @staticmethod
    def show_all_users():
        with DBManager() as db:
            query = """SELECT user_id, fullname, email, date_of_birth, gender, username, role,
            superuser, active, delete FROM users LIMIT 50;"""
            db.execute_query(query)
            return db.fetch_all()
    
    @staticmethod
    def delete_user(user_id):
        with DBManager() as db:
            query = """UPDATE users SET active = FALSE, delete = TRUE WHERE user_id = %s RETURNING user_id"""
            db.execute_query(query, (user_id,))
            db.commit_query()
            return db.fetch_one()

    @staticmethod
    def create_admin(fullname, email, date_of_birth, gender, username, password, superuser, position):
        password = hash_password(password)
        with DBManager() as db:
            query_users = """INSERT INTO users (fullname, email, date_of_birth, gender, username,
            password, role, superuser, active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, TRUE) RETURNING user_id"""
            query_admins = """INSERT INTO admins (user_id, position) VALUES (%s, %s) RETURNING user_id"""
            db.execute_query(query_users, (fullname, email, date_of_birth, gender, username,
                                           password, "admin", superuser))
            db.execute_query(query_admins, (db.fetch_one()[0], position))
            db.commit_query()
            return db.fetch_one()


class Doctor:
    
    @staticmethod
    def add_appointment(doctor_id, appointment_date, appointment_time, cost):
        with DBManager() as db:
            query = """INSERT INTO appointments (doctor_id, appointment_date, appointment_time,
            cost, available) VALUES (%s, %s, %s, %s, TRUE) RETURNING appointment_id"""
            db.execute_query(query, (doctor_id, appointment_date, appointment_time, cost))
            db.commit_query()
            return db.fetch_one()
    
    @staticmethod
    def show_doctor_visits(doctor_id):
        with DBManager() as db:
            query = """SELECT a.appointment_date, a.appointment_time, u.fullname FROM visits v JOIN
            appointments a ON v.appointment_id = a.appointment_id JOIN patients p ON v.patient_id 
            = p.patient_id JOIN users u ON p.user_id = u.user_id WHERE a.doctor_id = %s AND
            a.appointment_date >= CURRENT_DATE AND a.appointment_time > CURRENT_TIME"""
            db.execute_query(query, (doctor_id,))
            return db.fetch_all()

    def show_doctor_income(doctor_id):
        with DBManager() as db:
            query = """SELECT a.doctor_id, COUNT(v.visit_id) AS count_patients, SUM(a.cost) AS
            income FROM visits v JOIN appointments a ON v.appointment_id = a.appointment_id WHERE
            a.doctor_id = %s GROUP BY a.doctor_id;"""
            db.execute_query(query, (doctor_id,))
            return db.fetch_one()


class Patient:

    @staticmethod
    def show_all_doctors():
        with DBManager() as db:
            query = """SELECT d.doctor_id, u.fullname, d.specialization FROM users u JOIN doctors d
            ON u.user_id = d.user_id"""
            db.execute_query(query)
            return db.fetch_all()

    @staticmethod
    def show_doctor_appointments(doctor_id):
        with DBManager() as db:
            query = """SELECT a.appointment_id, a.appointment_date, a.appointment_time, a.cost
            FROM appointments a JOIN doctors d ON a.doctor_id = d.doctor_id WHERE a.available = TRUE
            AND d.doctor_id = %s"""
            db.execute_query(query, (doctor_id,))
            return db.fetch_all()

    @staticmethod
    def reserve_visit(appointment_id, patient_id):
        with DBManager() as db:
            query_visits = """INSERT INTO visits (appointment_id, patient_id, paid, paid_date)
            VALUES (%s, %s, TRUE, CURRENT_DATE)"""
            query_appointments = """UPDATE appointments SET available = FALSE WHERE appointment_id = %s"""
            db.execute_query(query_visits, (appointment_id, patient_id))
            db.execute_query(query_appointments, (appointment_id,))
            db.commit_query()

    @staticmethod
    def visit_history(patient_id):
        with DBManager() as db:
            query = """SELECT v.visit_id, a.appointment_date, a.appointment_time, a.cost, u.fullname as
            doctor FROM visits v JOIN appointments a ON v.appointment_id = a.appointment_id JOIN doctors
            d ON a.doctor_id = d.doctor_id JOIN users u ON d.user_id = u.user_id WHERE patient_id = %s;"""
            db.execute_query(query, (patient_id,))
            return db.fetch_all()


# ---- USER --------
# # User.sign_up_doctor
# User.sign_up_doctor("mobin snowa", "mobin@gmail.com", "2000-01-01", "male", "mobin", "1", "psycology", "123456783")

# # User.sign_up_patient
# User.sign_up_patient("bimar 10", "bimar10@gmail.com", "1999-09-09", "male", "bimar10", "1", 12345430)

# # User.sign_in
# result = User.sign_in("aliaryu", "1")
# print(result)

# ---- ADMIN --------
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

# # Admin.visits_info
# result = Admin.visits_info()
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

# # Admin.show_inactive_users
# result = Admin.show_inactive_users()
# titles = ["id", "fullname", "email", "date_of_birth", "gender", "username", "role", "superuser", "active", "delete"]
# for user in result:
#     print("\n----------\n")
#     for index, title in enumerate(titles):
#         print(title.ljust(30), user[index])

# # Admin.active_user
# Admin.active_user(2)

# # Admin.show_all_users
# result = Admin.show_all_users()
# titles = ["id", "fullname", "email", "date_of_birth", "gender", "username", "role", "superuser", "active", "delete"]
# for user in result:
#     print("\n----------\n")
#     for index, title in enumerate(titles):
#         print(title.ljust(30), user[index])

# # Admin.delete_user
# result = Admin.delete_user(2)
# print(result)

# # Admin.create_admin
# result = Admin.create_admin("donya monya", "donya@gmail.com", "1998-01-19", "female", "donya", "1", False, "watcher")
# print(result)

# ---- DOCTOR --------
# # Doctor.add_appointment
# Doctor.add_appointment(1, "2023-11-10", "11:00:00", 150)

# # Doctor.show_doctor_visits
# result = Doctor.show_doctor_visits(3)
# print("date".ljust(15), "time".ljust(15), "patient".ljust(20), "\n")
# for visit in result:
#     print(str(visit[0]).ljust(15), str(visit[1]).ljust(15), visit[2].ljust(20))

# # Doctor.show_doctor_income
# result = Doctor.show_doctor_income(3)
# print("count patients:".ljust(15), result[1])
# print("total income:".ljust(15), result[2])

# ---- PATIENT --------
# # Patient.show_all_doctors
# result = Patient.show_all_doctors()
# print("number".ljust(8), "fullname".ljust(20), "specialization".ljust(20), "\n")
# for index, doctor in enumerate(result):
#     print(str(index + 1).ljust(8), doctor[1].ljust(20), doctor[2].ljust(20))

# # Patient.show_doctor_appointments
# result = Patient.show_doctor_appointments(3)
# os.system("cls")
# print("number".ljust(8), "date".ljust(15), "time".ljust(15), "cost".ljust(10), "\n")
# for index, appointment in enumerate(result):
#     print(str(index + 1).ljust(8), str(appointment[1]).ljust(15), str(appointment[2]).ljust(15), str(appointment[3]).ljust(10))

# # Patient.reserve_visit
# Patient.reserve_visit(2, 9)

# # Patient.visit_history
# result = Patient.visit_history(9)
# print("visit_id".ljust(10), "date".ljust(15), "time".ljust(15), "cost".ljust(10), "doctor".ljust(20), "\n")
# for visit in result:
#     print(str(visit[0]).ljust(10), str(visit[1]).ljust(15), str(visit[2]).ljust(15), str(visit[3]).ljust(10), visit[4].ljust(20))
