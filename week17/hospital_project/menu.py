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
    def __init__(self, name):
        self.name = name
        self.items = []
        self.parent = None

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
            print("0: Exit\n")

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
                print(">>> bye bye ;*")
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
