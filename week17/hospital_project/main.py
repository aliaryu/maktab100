import sys
from pathlib import Path
project_folder = Path(__file__).resolve().parent
sys.path.append(str(project_folder))

from menu import Menu, Item
from database.database import User, Admin, Doctor
from datetime import datetime, timedelta
import os


# USER COOCKIES
# (1, 'ali aryu', 'aliaryu@yahoo.com', datetime.date(1997, 4, 22), 'male', 'aliaryu', <memory at 0x000001519434E5C0>, 'admin', True, True, False)
#  0     1               2                       3 hbd                4        5                    6 pw                 7      8s    9a    10d
user_info = None


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def show_sign_in():
    print("--- Sign-In Panel ---\n")
    username = input("Username: ")
    password = input("Password: ")
    global user_info
    user_info = User.sign_in(username,password)
    clear_terminal()
    if user_info:
        if user_info[9]:
            if not user_info[10]:
                print(f"Welcome to {user_info[7]} panel '{user_info[1].title()}' :D\n")
                if user_info[7] == "admin":
                    admin_menu.execute()
                elif user_info[7] == "doctor":
                    doctor_menu.execute()
                elif user_info[7] == "patient":
                    pass
            else:
                print("Your account has been deleted. Contact support.")
        else:
            print("Unfortunately, your account is not active.")
    else:
        print("Invalid username or password >_<")

def show_sign_up():
    role = input("Please Choice Registration AS:\n1: Patient\n2: Doctor\n\n >>> ")
    clear_terminal()
    if (role != "1") and (role != "2"):
        print("Invalid Input..")
        return
    print("--- Sign-Up Panel ---\n")
    fullname      = input("Full Name: ".ljust(40))
    gender        = input("Gender? (male or female): ".ljust(40)).lower()
    date_of_birth = input("Date Of Birth (e.g: 2001-01-01): ".ljust(40))
    print()
    email         = input("Email: ".ljust(40))
    username      = input("Username: ".ljust(40))
    password      = input("Password: ".ljust(40))
    password_r    = input("Password Repeat: ".ljust(40))
    if password == password_r:
        if role == "1":
            medical_record_number = input("Medical Record Number:".ljust(40))
            clear_terminal()
            try:
                User.sign_up_patient(fullname, email, date_of_birth, gender, username, password, medical_record_number)
                print(f"Your registration was successful '{fullname}'. Awaiting admin approval :D")
            except Exception as error:
                print("Unexpected Error:", "Invalid Inputs.\n", error)
        elif role == "2":
            specialization         = input("Specialization:".ljust(40))
            medical_license_number = input("Medical License Number:".ljust(40))
            clear_terminal()
            try:
                User.sign_up_doctor(fullname, email, date_of_birth, gender, username, password, specialization, medical_license_number)
                print(f"Your registration was successful '{fullname}'. Awaiting admin approval :D")
            except Exception as error:
                print("Unexpected Error:", "Invalid Inputs.\n", error)
    else:
        print("The passwords were not the same ;/")


def show_list_doctors():
    print("--- List Doctors ---\n")
    result = Admin.list_doctors()
    print("doctor_name".ljust(20), "date_of_birth".ljust(15), "gender".ljust(8), "specialization".ljust(20), "medical_license_number".ljust(20), "\n")
    for item in result:
        print(item[0].ljust(20), item[1].strftime("%Y-%m-%d").ljust(15), item[2].ljust(8), item[3].ljust(20), str(item[4]).ljust(20))
    input("\nPress 'Enter' to continue ...")
    clear_terminal()

def show_list_patients():
    print("--- List Patients ---\n")
    result = Admin.list_patients()
    print("doctor_name".ljust(20), "date_of_birth".ljust(15), "gender".ljust(8), "medical_record_number".ljust(10), "\n")
    for item in result:
        print(item[0].ljust(20), item[1].strftime("%Y-%m-%d").ljust(15), item[2].ljust(8), str(item[3]).ljust(10))
    input("\nPress 'Enter' to continue ...")
    clear_terminal()

def show_visits_info():
    print("--- Visit Info ---\n")
    result = Admin.visits_info()
    print("doctor_name".ljust(20), "specialization".ljust(20), "number_of_visits".ljust(20), "income".ljust(10), "\n")
    for item in result:
        print(item[0].ljust(20), item[1].ljust(20), str(item[2]).ljust(20), str(float(item[3])).ljust(10))
    input("\nPress 'Enter' to continue ...")
    clear_terminal()

def show_total_income():
    total_income_menu = Menu("Total Income", "Back", "")
    total_income_menu.add_item(Item("Daily Income", print, f"Daily Income: {Admin.income_daily()}"))
    total_income_menu.add_item(Item("Weekly Income", print, f"Weekly Income: {Admin.income_weekly()}"))
    total_income_menu.add_item(Item("Monthly Income", print, f"Monthly Income: {Admin.income_monthly()}"))
    total_income_menu.execute()
    clear_terminal()

def show_users_delete():
    if user_info[8]:
        print("--- Users/Delete ---\n")
        result = Admin.show_all_users()
        titles = ["id", "fullname", "email", "date_of_birth", "gender", "username", "role", "superuser", "active", "delete"]
        for user in result:
            print("\n----------\n")
            for index, title in enumerate(titles):
                print(title.ljust(30), user[index])
        while True:
            choice = input("\n1: Delete User\n0: Back\n\n >>> ")
            if choice == "1":
                clear_terminal()
                try:
                    user_id = int(input("Enter User ID: ".ljust(22)))
                except:
                    user_id = -1
                accept  = input("Are you sure? y/n: ".ljust(22)).lower()
                if accept in {"y", "ye", "yes"}:
                    output = Admin.delete_user(user_id)
                    if output:
                        clear_terminal()
                        print(f"User with ID '{user_id}' was deleted successfully :(")
                        break
                    else:
                        print("You entered a wrong ID -_-")
                else:
                    clear_terminal()
                    print("The delete process was canceled.")
                    break
            elif choice == "0":
                break
            else:
                clear_terminal()
                print("Invalid Input..\n")
    else:
        print("Sorry, Only superuser can delete users :]")

def show_inactive_users():
    result = Admin.show_inactive_users()
    if result:
        titles = ["id", "fullname", "email", "date_of_birth", "gender", "username", "role", "superuser", "active", "delete"]
        for user in result:
            print("\n----------\n")
            for index, title in enumerate(titles):
                print(title.ljust(30), user[index])
        while True:
            choice = input("\n1: Active User\n0: Back\n\n >>> ")
            if choice == "1":
                clear_terminal()
                try:
                    user_id = int(input("Enter User ID: ".ljust(22)))
                except:
                    user_id = -1
                accept  = input("Are you sure? y/n: ".ljust(22)).lower()
                if accept in {"y", "ye", "yes"}:
                    output = Admin.active_user(user_id)
                    if output:
                        clear_terminal()
                        print(f"User with ID '{user_id}' was actived successfully :p")
                        break
                    else:
                        print("You entered a wrong ID -_-")
                else:
                    clear_terminal()
                    print("The active process was canceled.")
                    break
            elif choice == "0":
                break
            else:
                clear_terminal()
                print("Invalid Input..\n")
    else:
        print("There are no inactive users -_-")

def show_create_admin():
    if user_info[8]:
        print("--- Create Admin ---\n")
        fullname      = input("Full Name: ".ljust(40))
        gender        = input("Gender? (male or female): ".ljust(40)).lower()
        date_of_birth = input("Date Of Birth (e.g: 2001-01-01): ".ljust(40))
        print()
        email         = input("Email: ".ljust(40))
        position      = input("Position: ".ljust(40))
        username      = input("Username: ".ljust(40))
        password      = input("Password: ".ljust(40))
        password_r    = input("Password Repeat: ".ljust(40))
        if password == password_r:
            superuser = input("Is SuperUser? y/n: ".ljust(40)).lower()
            if superuser in {"y", "ye", "yes"}:
                try:
                    output = Admin.create_admin(fullname, email, date_of_birth, gender, username, password, True, position)
                    clear_terminal()
                    if output:
                        print(f"User '{fullname}' was created in the role of 'admin' & 'superuser' O_O")
                    else:
                        print(f"Unexpected Error", "Invalid Inputs.\n")
                except Exception as error:
                    print("Unexpected Error:", "Invalid Inputs.\n", error)
            else:
                try:
                    output = Admin.create_admin(fullname, email, date_of_birth, gender, username, password, False, position)
                    clear_terminal()
                    if output:
                        print(f"User '{fullname}' was created in the role of 'admin' O_O")
                    else:
                        print(f"Unexpected Error", "Invalid Inputs.\n")
                except Exception as error:
                    print("Unexpected Error:", "Invalid Inputs.\n", error)
        else:
            print("The passwords were not the same ;/")
    else:
        print("Sorry, Only superuser can create admins :]")


def show_add_appointment():
    print("--- Add Appointment ---\n")
    current_date_time = datetime.now()
    print("Current Date & Time:".ljust(39), datetime.strftime(current_date_time, "%Y-%m-%d %H:%M:%S"))
    try:
        appointment_date = input("Appointment Date (e.g: 2001-01-01): ".ljust(40))
        if current_date_time.date() > datetime.strptime(appointment_date, "%Y-%m-%d").date():
            clear_terminal()
            print("Invalid Date.. You cannot choose a date in the past.")
            return
    except:
        clear_terminal()
        print("Invalid Date Format..")
        return
    try:
        appointment_time = input("Appointment Time (e.g: 08:00:00): ".ljust(40))
        if current_date_time.date() == datetime.strptime(appointment_date, "%Y-%m-%d").date():
            if current_date_time.time() > datetime.strptime(appointment_time, "%H:%M:%S").time():
                clear_terminal()
                print("Invalid Time.. You cannot choose a time in the past.")
                return
    except:
        clear_terminal()
        print("Invalid Time Format..")
        return
    try:
        cost = float(input("Cost: ".ljust(40)))
        if cost <= 0:
            clear_terminal()
            print("Invalid Cost.. You cannot enter a negative or zero cost.")
            return
    except:
        clear_terminal()
        print("Invalid Cost Format..")
        return
    clear_terminal()
    print(f"Appointment time on '{appointment_date} {appointment_time}' date &\ntime with a cost of '{cost}'. do you confirm?")
    choice = input("\ny/n: ").lower()
    if choice in {"y", "ye", "yes"}:
        output = Doctor.add_appointment(user_info[0], appointment_date, appointment_time, cost)
        clear_terminal()
        if output:
            print("The appointment was successfully registered in the system ^^")
        else:
            print(f"Unexpected Error", "Invalid Inputs.\n")
    else:
        print("Appointment registration was canceled.")

def show_doctor_visits():
    print("--- My Visits ---\n")
    try:
        result = Doctor.show_doctor_visits(Doctor.get_doctor_id_by_user_id(user_info[0]))
        if result:
            print("date".ljust(15), "time".ljust(15), "patient".ljust(20), "\n")
            for visit in result:
                print(str(visit[0]).ljust(15), str(visit[1]).ljust(15), visit[2].ljust(20))
        else:
            print("No visits have been registered :(")
        input("\nPress 'Enter' to continue ...")
        clear_terminal()
    except Exception as error:
        print("Unexpected Error:", "Invalid Inputs.\n", error)

def show_doctor_income():
    print("--- My Income ---\n")
    result = Doctor.show_doctor_income(3)
    if result:
        print("count patients:".ljust(20), result[1])
        print("total income:".ljust(20), result[2])
    else:
        print("You have not received any income yet :(")
    input("\nPress 'Enter' to continue ...")
    clear_terminal()





def show_contact():
    print("Phone:".ljust(10), "+84 32 22 1600")
    print("Email:".ljust(10), "avicenna@support.com")
    print("Postal:".ljust(10), "6031345011")
    print("Fax:".ljust(10), "+84 32 22 4444")
    print("Address:".ljust(10), "Milky Way, Solar System, Heaven ;)")
    input("\nPress 'Enter' to continue ...")
    clear_terminal()

def show_about():
    about = r'''
                                    _ _.-'`-._ _
                                   ;.'________'.;
                        _________n.[____________].n_________
                       |""_""_""_""||==||==||==||""_""_""_""]
                       |"""""""""""||..||..||..||"""""""""""|
                       |LI LI LI LI||LI||LI||LI||LI LI LI LI|
                       |.. .. .. ..||..||..||..||.. .. .. ..|
                       |LI LI LI LI||LI||LI||LI||LI LI LI LI|
                    ,,;;,;;;,;;;,;;;,;;;,;;;,;;;,;;,;;;,;;;,;;,,
                   ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

                              -- Avicenna Hospital --

    Born out of the former Ebnesina clinic in June 2001, Ebnesina Hospital, (named after
    Avicenna or Ibn Sina, the great Iranian polymath and physician of the 10th century,)
    is located in Earth district in the west of Heaven; (Ebnesian clinic was itself
    established in 1973).
    
                          Designed by:  aliaryu@yahoo.com
    '''
    print(about)
    input("\nPress 'Enter' to continue ...")
    clear_terminal()


# MAIN MENU
main_menu = Menu("Avicenna Hospital", exit_message="Your health is our goal <3 Bye.\n")
main_menu.add_item(Item("Sign-In", show_sign_in))
main_menu.add_item(Item("Sign-Up", show_sign_up))
main_menu.add_item(Item("Contact", show_contact))
main_menu.add_item(Item("About", show_about))

# ADMIN MENU
admin_menu = Menu("Admin", "Logout", "Bye Bye ;*")
admin_menu.add_item(Item("List Doctors", show_list_doctors))
admin_menu.add_item(Item("List Patients", show_list_patients))
admin_menu.add_item(Item("Visits Info", show_visits_info))
admin_menu.add_item(Item("Total Income", show_total_income))
admin_menu.add_item(Item("Inactive Users", show_inactive_users))
admin_menu.add_item(Item("Users/Delete", show_users_delete))
admin_menu.add_item(Item("Create Admin", show_create_admin))

# DOCTOR MENU
doctor_menu = Menu("Doctor", "Logout", "Bye Bye Dr.")
doctor_menu.add_item(Item("Add Appointment", show_add_appointment))
doctor_menu.add_item(Item("Show My Visits", show_doctor_visits))
doctor_menu.add_item(Item("Show My Income", show_doctor_income))

# PATIENT MENU
patient_menu = Menu("Patient", "Logout", "God Bles You.. Bye.")
patient_menu.add_item(Item("Reserve Visit", show_reserve_visit))

if __name__ == "__main__":
    main_menu.execute()