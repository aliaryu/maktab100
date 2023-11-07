import sys
from pathlib import Path
project_folder = Path(__file__).resolve().parent
sys.path.append(str(project_folder))

from menu import Menu, Item
from database.database import User
import os


# USER COOCKIES
# (1, 'ali aryu', 'aliaryu@yahoo.com', datetime.date(1997, 4, 22), 'male', 'aliaryu', <memory at 0x000001519434E5C0>, 'admin', True, True, False)
#  0     1               2                       3 hbd                4        5                    6 pw                 7      8s    9a    10d
user_info = None



def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def show_sign_in():
    username = input("Username: ")
    password = input("Password: ")
    global user_info
    user_info = User.sign_in(username,password)
    clear_terminal()
    if user_info:
        print(f"Welcome to {user_info[7]} panel '{user_info[1].title()}' :D\n")
        if user_info[7] == "admin":
            admin_menu.execute()
        elif user_info[7] == "doctor":
            pass
        elif user_info[7] == "patient":
            pass
    else:
        print("Invalid username or password >_<")

def show_sign_up():
    pass





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


if __name__ == "__main__":
    main_menu.execute()