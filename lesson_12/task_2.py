import requests
from pprint import pprint

STARWARS_API_URL = 'https://swapi.dev/api/'
get_ship = requests.get(STARWARS_API_URL + 'starships/10/')


class Starship:
    def __init__(self, name, speed, starship_class, pilots):
        self.name = name
        self.speed = speed
        self.starship_class = starship_class
        self.pilots = pilots

    def pilots_info(self, pilot_url):
        pilots_data = requests.get(pilot_url).json()
        pilot_info = {
            'name': pilots_data['name'],
            'height': pilots_data['height'],
            'mass': pilots_data['mass'],
            'homeworld': pilots_data['homeworld'],
            'homeworld_url': pilots_data['homeworld']
        }
        return pilot_info

    def ship_info(self):
        ship_data = get_ship.json()
        self.name = ship_data['name']
        self.speed = ship_data['max_atmosphering_speed']
        self.starship_class = ship_data['starship_class']
        self.pilots = []

        for pilot_url in ship_data['pilots']:
            pilot_info = self.pilots_info(pilot_url)
            self.pilots.append(pilot_info)

        return {
            "name": self.name,
            "max_atmosphering_speed": self.speed,
            "starship_class": self.starship_class,
            "pilots": self.pilots
        }


millennium_falcon = Starship('', '', '', [])
ship_info = millennium_falcon.ship_info()
pprint(ship_info)
