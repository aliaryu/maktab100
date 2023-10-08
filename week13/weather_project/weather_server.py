from typing import Union
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json
import os
os.system("cls" if os.name == "nt" else "clear")


def get_city_weather(city_name: str) -> Union[dict, str]:
    """
    This function retrieve weather data from an external API for a given city.

    Args:
        - city_name (str): The name of the city to retrieve weather data for.
    Returns:
        - dict: A dictionary containing weather information for the city,
        including temperature, feels like temperature, and last updated time.
        - str: If an error occurs in the process of the function, a string of
        the error that occurred is returned
    """

    # CONFIGS - according to document https://www.weatherapi.com
    url     = "http://api.weatherapi.com/v1/current.json"
    api_key = "36da30a8c7654537b83181509230710"
    params  = {"key":api_key, "q":city_name, "aqi":"no"}

    # REQUEST MANAGER
    with requests.Session() as r:
        r = requests.get(url, params=params)
        data = r.json()

        if r.status_code == 200:
            return {
                "temperature" : data["current"]["temp_c"],
                "feels_like"  : data["current"]["feelslike_c"],
                "last_updated": data["current"]["last_updated"]
            }
        else:
            return data["error"]["message"]


class ServerRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # This conditional statements handling what content type added to page
        if self.path.endswith(".css"):
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            with open("web/style.css", "r") as file:
                data = file.read()
            self.wfile.write(bytes(data, "utf-8"))
        elif self.path.endswith((".jpg", ".png", ".gif")):
            image_path = "web" + self.path
            content_type = "image/jpeg" if self.path.endswith(".jpg") else "image/png" if self.path.endswith(".png") else "image/gif"
            self.send_response(200)
            self.send_header("Content-type", content_type)
            self.end_headers()
            with open(image_path, "rb") as file:
                data = file.read()
            self.wfile.write(data)
        elif self.path.endswith(".js"):
            self.send_response(200)
            self.send_header("Content-type", "application/javascript")
            self.end_headers()
            with open("web/script.js", "r") as file:
                data = file.read()
            self.wfile.write(bytes(data, "utf-8"))
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("web/index.html", "r") as file:
                data = file.read()
            self.wfile.write(bytes(data, "utf-8"))


    # For test in terminal: curl 192.168.1.101:8000 -X POST -d "city_name=london"
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')

        parameters = parse_qs(body)
        weather = get_city_weather(parameters["city_name"][0])

        if isinstance(weather, str):
            self.send_response(404)
        else:
            self.send_response(200)
        
        self.send_header("Content-type", "application/json")
        self.end_headers()
        data = json.dumps(weather)
        self.wfile.write(bytes(data, "utf-8"))


def start_server() -> None:
    """
    This function starts the weather server on localhost.
    """

    # CONFIGS - according ipv4 or ipv6 and a free port
    host = "192.168.1.101"
    port = 8000
    server = HTTPServer((host, port), ServerRequestHandler)

    try:
        emoji = "⣿⣸⠈⠄⠄⠰⠾⠴⢾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⣾⢀⠁⠄⠄⠄⢠⢸⣿⣿\n⣿⣿⣆⠄⠆⠄⣦⣶⣦⣌⣿⣿⣿⣿⣷⣋⣀⣈⠙⠛⡛⠌⠄⠄⠄⠄⢸⢸⣿⣿\n⣿⣿⣿⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠈⠄⠄⠄⠄⠄⠈⢸⣿⣿\n⣿⣿⣿⠄⠄⠄⠘⣿⣿⣿⡆⢀⣈⣉⢉⣿⣿⣯⣄⡄⠄⠄⠄⠄⠄⠄⠄⠈⣿⣿\n⣿⣿⡟⡜⠄⠄⠄⠄⠙⠿⣿⣧⣽⣍⣾⣿⠿⠛⠁⠄⠄⠄⠄⠄⠄⠄⠄⠃⢿⣿"
        print(emoji)
        print(f"Server Running on 'http://{host}:{port}'")
        print("For stop server use 'Ctrl+C' or kill terminal.")
        print("...")
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("...")
        print("Server Stopped.")


if __name__ == "__main__":  
    start_server()
