import os
os.system("cls" if os.name == "nt" else "clear")


class Item:
    def __init__(self, name, action, *args):
        self.name = name
        self.action = action
        self.args = args

    def execute(self):
        if self.args:
            self.action(*self.args)
        else:
            self.action()


class Menu:
    def __init__(self, name, exit_menu="Exit", exit_message="bye bye ;*"):
        self.name = name
        self.items = []
        self.parent = None
        self.exit_menu = exit_menu
        self.exit_message = exit_message

    def add_item(self, item):
        self.items.append(item)
        if isinstance(item, Menu):
            item.parent = self

    def execute(self):
        print(f"{self.name} Menu:")
        for index, item in enumerate(self.items):
            print(f"{index + 1}: {item.name}")
        if self.parent:
            print("0: Back\n")
        else:
            print(f"0: {self.exit_menu}\n")

        try:
            choice = int(input(">>> "))
        except:
            choice = -1

        if choice == 0:
            if self.parent:
                os.system("cls" if os.name == "nt" else "clear")
                self.parent.execute()
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print(f">>> {self.exit_message}")
        elif 1 <= choice <= len(self.items):
            item = self.items[choice - 1]
            if isinstance(item, Item):
                os.system("cls" if os.name == "nt" else "clear")
                item.execute()
                print()
                self.execute()
                
            elif isinstance(item, Menu):
                os.system("cls" if os.name == "nt" else "clear")
                item.execute()
                print()
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Invalid input..\n")
            self.execute()
