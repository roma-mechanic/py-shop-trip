import json
import math

from shops import Shops


class Customers:
    def __init__(self, customer_dict: dict) -> None:
        self.name = customer_dict["name"]
        self.prod_cart = customer_dict["product_cart"]
        self.location = customer_dict["location"]
        self.money = customer_dict["money"]
        self.car = customer_dict["car"]

    @staticmethod
    def distance_two_points(point_1: list, point_2: list):
        x1, y1 = point_1
        x2, y2 = point_2
        return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)

    def calc_trip(self, market_list: Shops):
        dict_distance = {}
        for market in market_list.list_of_shops:
            dict_distance[market.name] = self.distance_two_points(market.location, self.location)
        min_distance = min(dict_distance.values())
        final_dict = {k: v for k, v in dict_distance.items() if v == min_distance}
        return final_dict

    #
    #         name_of_nearest_shop = min(distance_to_shops, key=lambda unit: distance_to_shops[unit])


if __name__ == "__main__":
    # customers = [
    #     {
    #         "name": "Bob",
    #         "product_cart": {
    #             "milk": 4,
    #             "bread": 2,
    #             "butter": 5
    #         },
    #         "location": [12, -2],
    #         "money": 55,
    #         "car": {
    #             "brand": "Suzuki",
    #             "fuel_consumption": 9.9
    #         }
    #     },
    #     {
    #         "name": "Alex",
    #         "product_cart": {
    #             "milk": 2,
    #             "bread": 2,
    #             "butter": 2
    #         },
    #         "location": [1, -2],
    #         "money": 41,
    #         "car": {
    #             "brand": "BMW",
    #             "fuel_consumption": 9.1
    #         }
    #     },
    #     {
    #         "name": "Monica",
    #         "product_cart": {
    #             "milk": 3,
    #             "bread": 3,
    #             "butter": 1
    #         },
    #         "location": [11, -2],
    #         "money": 12,
    #         "car": {
    #             "brand": "Audi",
    #             "fuel_consumption": 7.6
    #         }
    #     }
    # ]
    with open("config.json", "r") as data_file:
        config_file = json.load(data_file)

        for shop in config_file["shops"]:
            market = Shops(shop)
        for customer in config_file["customers"]:
            person = Customers(customer)
            print(person.calc_trip(market))
