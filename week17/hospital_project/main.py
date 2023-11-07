import sys
from pathlib import Path
project_folder = Path(__file__).resolve().parent
sys.path.append(str(project_folder))

from menu import Menu, Item
from database.database import User
import os


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def show_sign_in():
    pass

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







main = Menu("Avicenna Hospital")

main.add_item(Item("Sign-In", show_sign_in))
main.add_item(Item("Sign-Up", show_sign_up))

main.add_item(Item("Contact", show_contact))
main.add_item(Item("About", show_about))

main.execute()