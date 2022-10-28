
from errors import FullRangeOfGoods
from store import Store


class Shop(Store):
    def __init__(self, items: dict[str, int], capacity: int = 20, product_variety: int = 5):
        super().__init__(items, capacity)
        self._product_variety = product_variety

    @property
    def product_variety(self):
        return self._product_variety

    def add(self, title, quantity):
        number_of_products = len(self.get_items().keys())
        if number_of_products >= self.product_variety:
            raise FullRangeOfGoods
        return super().add(title, quantity)


# shop_dict = {}
# shop = Shop(shop_dict)
# print(shop.add('abc', 5))
# print(shop.add('abc', 5))
# print(shop.add('cde', 5))
# print(shop.remove('cde', 5))
# print(shop.add('sdf', 5))
# print(shop.add('awerbc', 5))
# print(shop.add('wer', 5))
# print(shop.add('dfg', 5))
# print(shop.add('fgh', 5))
