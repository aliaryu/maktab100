from typing import Union
from menu import Menu, Item
import requests
from ipv4 import get_ipv4
import os
os.system("cls" if os.name == "nt" else "clear")


def get_weather(city_name: str) -> Union[dict, str]:
    """
    This function gets weather data, including temperature,
    feels like temperature, and last updated time for a city
    """
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


def show_weather() -> None:
    """This function is an Action for menu"""
    os.system("cls" if os.name == "nt" else "clear")
    city = input("City: ")

    data = get_weather(city)
    if isinstance(data, dict):
        for key, value in data.items():
            print(key, value)
    else:
        print(data)


def get_request_count() -> int:
    """This function gets the number of requests in server"""
    url = f"http://{get_ipv4()}:8000/get_request_count"
    try: 
        with requests.Session() as r:
            r = requests.post(url)
            return r.json()
    except requests.exceptions.ConnectionError:
        return "Connection Error - maybe server is off?"
    except Exception as error:
        return 'Unexpected Error o_o"'


def show_request_count() -> None:
    """This function is an Action for menu"""
    os.system("cls" if os.name == "nt" else "clear")
    data = get_request_count()
    if isinstance(data, dict):
        print("Count Requests: ", data.values()[0])
    else:
        print("Count Requests: ",data)


def start_client() -> None:
    """
    This function starts the weather client command-line interface.
    Used cli menu to create interface for interact in terminal.
    """
    
    main_menu = Menu("Main")

    item_weather = Item("Weather", show_weather)
    main_menu.add_item(item_weather)

    item_count_requests = Item("Count Requests", show_request_count)
    main_menu.add_item(item_count_requests)

    main_menu.display()
    main_menu.execute()


if __name__ == "__main__":
    start_client()
    emoji = "⢠⢕⠅⣾⣿⠋⢿⣿⣿⣿⠉⣿⣿⣷⣦⣶⣽⣿⣿⠈⣿⣿⣿⣿⠏⢹⣷⣷⡅⢐\n⣔⢕⢥⢻⣿⡀⠈⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠛⠛⠁ ⣼⣿⣿⡇⢔\n⢕⢕⢽⢸⢟⢟⢖⢖⢤⣶⡟⢻⣿⡿⠻⣿⣿⡟⢀⣿⣦⢤⢤⢔⢞⢿⢿⣿⠁⢕\n⢕⢕⠅⣐⢕⢕⢕⢕⢕⣿⣿⡄⠛⢀⣦⠈⠛⢁⣼⣿⢗⢕⢕⢕⢕⢕⢕⡏⣘⢕\n⢕⢕⠅⢓⣕⣕⣕⣕⣵⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣕⢕⢕⢕⢕⡵⢀⢕⢕"
    print(emoji)
