from menu import Menu, Item
import requests
from ipv4 import get_ipv4
import os
os.system("cls" if os.name == "nt" else "clear")


def get_weather(city_name: str) -> dict:
    """
    This function gets weather data, including temperature,
    feels like temperature, and last updated time for a city
    """

    # CONFIGS
    url = f"http://{get_ipv4()}:8000/"
    params = {"city_name": city_name}

    try: 
        with requests.Session() as r:
            r = requests.post(url, data=params)
            return r.json()
    except requests.exceptions.ConnectionError:
        return "Connection Error - maybe server is off?"
    except Exception as error:
        return 'Unexpected Error o_o"'


def show_weather():
    os.system("cls" if os.name == "nt" else "clear")
    city = input("City: ")

    data = get_weather(city)
    if isinstance(data, dict):
        for key, value in data.items():
            print(key, value)
    else:
        print(data)





def start_client() -> None:
    """
    This function starts the weather client command-line interface.
    Used cli menu to create interface for interact in terminal.
    """
    
    main_menu = Menu("Main")

    item_weather = Item("Weather", show_weather)
    main_menu.add_item(item_weather)

    main_menu.display()
    main_menu.execute()


if __name__ == "__main__":
    start_client()
    emoji = "⢠⢕⠅⣾⣿⠋⢿⣿⣿⣿⠉⣿⣿⣷⣦⣶⣽⣿⣿⠈⣿⣿⣿⣿⠏⢹⣷⣷⡅⢐\n⣔⢕⢥⢻⣿⡀⠈⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠛⠛⠁ ⣼⣿⣿⡇⢔\n⢕⢕⢽⢸⢟⢟⢖⢖⢤⣶⡟⢻⣿⡿⠻⣿⣿⡟⢀⣿⣦⢤⢤⢔⢞⢿⢿⣿⠁⢕\n⢕⢕⠅⣐⢕⢕⢕⢕⢕⣿⣿⡄⠛⢀⣦⠈⠛⢁⣼⣿⢗⢕⢕⢕⢕⢕⢕⡏⣘⢕\n⢕⢕⠅⢓⣕⣕⣕⣕⣵⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣕⢕⢕⢕⢕⡵⢀⢕⢕"
    print(emoji)
