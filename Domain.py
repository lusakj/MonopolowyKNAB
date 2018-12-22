import math
import json


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, x, y):
        distance = math.sqrt((x-self.x)**2 + (y-self.y)**2)
        return round(distance, 2)



class Shop:
    def __init__(self, name, coordinates, products):
        self.name = name
        self.coordinates = coordinates
        self.products = products

    def find_products(self, starting_string):
        found_products =[ ]
        for product in self.products:
            if starting_string in product.name:
                found_products.append(product)

        return found_products


class Model:
    def __init__(self):
        with open('data.json', 'r') as outfile:
            self.shops = self.__to_objects(json.load(outfile))

    def __to_objects(self, shops_jsons):
        objects = []
        for shop_json in shops_jsons:
            objects.append(Shop(shop_json["name"],
                                self.__to_coordinates(shop_json["coordinates"]),
                                self.__to_products(shop_json["products"])))
        return objects

    def __to_coordinates(self, coordinates_json):
        return Coordinates(coordinates_json["x"], coordinates_json["y"])

    def __to_products(self, products_jsons):
        products = []
        for product in products_jsons:
            products.append(Product(product["name"], product["price"]))
        return products

    def search(self, starting_string):
        found_shops = []
        for shop in self.shops:
            in_shop = shop.find_products(starting_string)
            if len(in_shop) != 0:
                found_shops.append(Shop(shop.name, shop.coordinates, in_shop))
        sorted_by_distance = self.sort_shops_distance(found_shops)

        return sorted_by_distance

    def sort_shops_name(self, found_shops):
        sorted_by_name = sorted(found_shops, key=lambda shop: shop.name, reverse=True)
        return sorted_by_name

    def sort_shops_price(self, found_shops):
        sorted_by_price = sorted(found_shops, key=lambda shop: shop.name)
        return sorted_by_price

    def sort_shops_distance(self, found_shops):
        sorted_by_distance = sorted(found_shops, key=lambda shop: shop.coordinates.calculate_distance(0,0))
        return sorted_by_distance













