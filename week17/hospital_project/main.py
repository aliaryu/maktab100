import sys
from pathlib import Path
project_folder = Path(__file__).resolve().parent
sys.path.append(str(project_folder))

from menu import Menu, Item
from database.database import User, Admin
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
                    pass
                elif user_info[7] == "doctor":
                    pass
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
        print("Wrong Input...")
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
    print("fullname".ljust(20), "date_of_birth".ljust(15), "gender".ljust(8), "specialization".ljust(20), "medical_license_number".ljust(20), "\n")
    for item in result:
        print(item[0].ljust(20), item[1].strftime("%Y-%m-%d").ljust(15), item[2].ljust(8), item[3].ljust(20), str(item[4]).ljust(20))
    input("\nPress 'Enter' to continue ...")
    clear_terminal()

def show_list_patients():
    print("--- List Patients ---\n")
    result = Admin.list_patients()
    print("fullname".ljust(20), "date_of_birth".ljust(15), "gender".ljust(8), "medical_record_number".ljust(10), "\n")
    for item in result:
        print(item[0].ljust(20), item[1].strftime("%Y-%m-%d").ljust(15), item[2].ljust(8), str(item[3]).ljust(10))
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
main_menu = Menu("Avicenna Hospital", exit_message="Your health is our goal <3 Bye.")
main_menu.add_item(Item("Sign-In", show_sign_in))
main_menu.add_item(Item("Sign-Up", show_sign_up))
main_menu.add_item(Item("Contact", show_contact))
main_menu.add_item(Item("About", show_about))

# ADMIN MENU
admin_menu = Menu("Admin", "Logout", "Bye Bye ;*")
admin_menu.add_item(Item("List Doctors", show_list_doctors))
admin_menu.add_item(Item("List Patients", show_list_patients))


if __name__ == "__main__":
    main_menu.execute()