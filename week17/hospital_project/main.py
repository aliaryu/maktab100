from menu import Menu, Item
import os


def show_contact():
    print("Phone:".ljust(10), "+84 32 22 1600")
    print("Email:".ljust(10), "avicenna@support.com")
    print("Postal:".ljust(10), "14516167")
    print("Fax:".ljust(10), "843222")
    print("Address:".ljust(10), "Milky Way, Solar System, Heaven ;)")
    input("\nPress 'Enter' to continue ...")
    os.system("cls" if os.name == "nt" else "clear")









main = Menu("Avicenna Hospital")

main.add_item(Item("Contact", show_contact))


main.execute()