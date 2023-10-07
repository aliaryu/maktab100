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
        if isinstance(item, Item):
            self.items.append(item)
        elif isinstance(item, Menu):
            item.parent = self
            self.items.append(item)

    def display(self):
        print(f"{self.name} Menu:")
        for index, item in enumerate(self.items):
            print(f"{index + 1}: {item.name}")
        if self.parent:
            print("0: Back\n")
        else:
            print("0: Exit\n")

    def execute(self):
        try:
            choice = int(input(">>> "))
        except:
            choice = -1

        if choice == 0:
            if self.parent:
                os.system("cls")
                self.parent.display()
                self.parent.execute()
            else:
                print(">>> bye bye ;*")
        elif 1 <= choice <= len(self.items):
            item = self.items[choice - 1]
            if isinstance(item, Item):
                os.system("cls")
                item.execute()
                print()
                self.display()
                self.execute()
                
            elif isinstance(item, Menu):
                os.system("cls")
                item.display()
                item.execute()
                print()
        else:
            os.system("cls")
            print("Invalid input..\n")
            self.display()
            self.execute()
