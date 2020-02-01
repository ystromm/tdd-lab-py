from price_api import PriceApi

class ShoppingCart:
    def __init__(self):
        self.total = 0.0
        self.i = 0

    def get_nr_of_items(self):
        return self.i

    def add_item(self, item):
        self.i += 1
        self.total += item.price

    def remove_item(self, item):
        self.i -= 1

    def get_total(self):
        return self.total
