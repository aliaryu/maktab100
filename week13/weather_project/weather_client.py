from typing import Union, List, Tuple
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
        input("\nPress 'Enter' to back to the menu ^^\n>>> ")
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print(data)


def get_request_count() -> int:
    """This function gets the number of requests in server"""
    url = f"http://{get_ipv4()}:8000/get_request_count"
    try: 
        with requests.Session() as r:
            r = requests.post(url)
            return int(r.json())
    except requests.exceptions.ConnectionError:
        return "Connection Error - maybe server is off?"
    except Exception as error:
        return 'Unexpected Error o_o"'


def show_request_count() -> None:
    """This function is an Action for menu"""
    data = get_request_count()
    if isinstance(data, int):
        print("Count Requests:", data)
    else:
        print(data)


def get_successful_request_count() -> int:
    """This function gets the number of successful requests in server"""
    url = f"http://{get_ipv4()}:8000/get_successful_request_count"
    try: 
        with requests.Session() as r:
            r = requests.post(url)
            return int(r.json())
    except requests.exceptions.ConnectionError:
        return "Connection Error - maybe server is off?"
    except Exception as error:
        return 'Unexpected Error o_o"'


def get_count_requests_by_city() -> List[List]:
    """This function gets requests count group by city in server"""
    url = f"http://{get_ipv4()}:8000/get_count_requests_by_city"
    try: 
        with requests.Session() as r:
            r = requests.post(url)
            return r.json()
    except requests.exceptions.ConnectionError:
        return "Connection Error - maybe server is off?"
    except Exception as error:
        return 'Unexpected Error o_o"'


def show_count_requests_by_city():
    """This function is an Action for menu"""
    data = get_count_requests_by_city()
    if isinstance(data, list):
        if data:
            for city_number in data:
                print(city_number[0].ljust(20), city_number[1])
            input("\nPress 'Enter' to back to the menu ^^\n>>> ")
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("There is no data yet :D")
    else:
        print(data)


def show_successful_request_count():
    """This function is an Action for menu"""
    data = get_successful_request_count()
    if isinstance(data, int):
        print("Count Successful Requests:", data)
    else:
        print(data)


def get_last_hour_requests() -> List[List]:
    """This function gets last hour requests in server"""
    url = f"http://{get_ipv4()}:8000/get_last_hour_requests"
    try: 
        with requests.Session() as r:
            r = requests.post(url)
            return r.json()
    except requests.exceptions.ConnectionError:
        return "Connection Error - maybe server is off?"
    except Exception as error:
        return 'Unexpected Error o_o"'


def show_last_hour_requests():
    """This function is an Action for menu"""
    data = get_last_hour_requests()
    if isinstance(data, list):
        if data:
            for city_date in data:
                print(city_date[0].ljust(20), city_date[1])
            input("\nPress 'Enter' to back to the menu ^^\n>>> ")
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("There is no data yet :D")
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

    item_count_requests = Item("Count Requests", show_request_count)
    main_menu.add_item(item_count_requests)

    item_count_successful_requests = Item("Count Successful Requests", show_successful_request_count)
    main_menu.add_item(item_count_successful_requests)

    item_count_requests_by_city = Item("Count City Requests", show_count_requests_by_city)
    main_menu.add_item(item_count_requests_by_city)

    item_last_hour_requests = Item("Last Hour Requests", show_last_hour_requests)
    main_menu.add_item(item_last_hour_requests)

    main_menu.display()
    main_menu.execute()


if __name__ == "__main__":
    start_client()
    emoji = "⢠⢕⠅⣾⣿⠋⢿⣿⣿⣿⠉⣿⣿⣷⣦⣶⣽⣿⣿⠈⣿⣿⣿⣿⠏⢹⣷⣷⡅⢐\n⣔⢕⢥⢻⣿⡀⠈⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠛⠛⠁ ⣼⣿⣿⡇⢔\n⢕⢕⢽⢸⢟⢟⢖⢖⢤⣶⡟⢻⣿⡿⠻⣿⣿⡟⢀⣿⣦⢤⢤⢔⢞⢿⢿⣿⠁⢕\n⢕⢕⠅⣐⢕⢕⢕⢕⢕⣿⣿⡄⠛⢀⣦⠈⠛⢁⣼⣿⢗⢕⢕⢕⢕⢕⢕⡏⣘⢕\n⢕⢕⠅⢓⣕⣕⣕⣕⣵⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣕⢕⢕⢕⢕⡵⢀⢕⢕"
    print(emoji)
