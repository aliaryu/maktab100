import requests
from http.server import HTTPServer, BaseHTTPRequestHandler

import os
os.system("cls" if os.name == "nt" else "clear")


def get_city_weather(city_name: str) -> dict:
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
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("hi", "utf-8"))


def start_server() -> None:
    """
    This function starts the weather server on localhost.
    """
    host = "192.168.1.101"
    port = 8000
    server = HTTPServer((host, port), ServerRequestHandler)
    try:
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
