import sys
from pathlib import Path
project_folder = Path(__file__).resolve().parent
sys.path.append(str(project_folder))


from menu import Menu, Item
from database.database import User
import os


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
    os.system("cls" if os.name == "nt" else "clear")

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

    At the time of unpaved streets in Heaven, the residents of the neighborhood used
    to trust in one name only when they had medical problems, and that was “Ebnesina”.
    Despite the construction of a dozen medical centers within the same area over the
    past few decades, Ebnesian Hospital is still the most reputable medical center,
    giving services to more than 1000 patients per day.Today, after the passage of more
    than 11 years from the conversion of Ebnesina clinic to Ebnesina Hospital, the
    center has enhanced its capabilities and facilities to offer more professional and
    up-to-date medical services and complicated surgeries.Ebnesina Hospital boasts a
    host of experienced staff & medical doctors as well as the latest medical equipment
    based on the international standards that are utilized to offer the best and most
    affordable services to patients.The International Patients Department (IPD) of
    Ebnesina Hospital is specially equipped for admitting foreign patients in accordance
    with the medical tourism rules and regulations of the Ministry of Health of Heaven.
    
                           Designed by: aliaryu@yahoo.com
    '''
    print(about)
    input("\nPress 'Enter' to continue ...")
    os.system("cls" if os.name == "nt" else "clear")







main = Menu("Avicenna Hospital")

main.add_item(Item("Sign-In", show_sign_in))
main.add_item(Item("Sign-Up", show_sign_up))

main.add_item(Item("Contact", show_contact))
main.add_item(Item("About", show_about))

main.execute()