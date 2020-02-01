import unittest
from unittest.mock import patch

import items
from shopping_cart import ShoppingCart


class ShoppingCartTest(unittest.TestCase):
    def test_empty_shoppingcart_should_be_empty(self):
        self.assertEqual(ShoppingCart().get_nr_of_items(), 0)

    def test_empty_shoppingcart_should_have_total(self):
        self.assertEqual(ShoppingCart().get_total(), 0)

    @patch("shopping_cart.PriceApi")
    def test_empty_shoppingcart_should_not_get_price(self, price_api):
        self.assertEqual(ShoppingCart().get_total(), 0)
        price_api.assert_not_called()

    def test_shoppingcart_with_item_added_should_contain_one_item(self):
        shopping_cart = ShoppingCart()
        shopping_cart.add_item(items.BANAN)
        self.assertEqual(shopping_cart.get_nr_of_items(), 1)

    def test_shoppingcart_with_item_added_and_removed_should_be_empty(self):
        shopping_cart = ShoppingCart()
        shopping_cart.add_item(items.BANAN)
        shopping_cart.remove_item(items.BANAN)
        self.assertEqual(shopping_cart.get_nr_of_items(), 0)

    def test_shoppingcart_with_item_added_should_have_total(self):
        shopping_cart = ShoppingCart()
        shopping_cart.add_item(items.BANAN)
        self.assertEqual(shopping_cart.get_total(), items.BANAN.price)


if __name__ == '__main__':
    unittest.main()
