from errors import NoFreeSpace, NothingToRemove, LowQuantityOfProduct
from storage import Storage


class Store(Storage):
    def __init__(self, items: dict[str, int], capacity: int = 100):
        self._items = items
        self._capacity = capacity

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, title, quantity):
        free_space = self.get_free_space()
        if free_space == 0 or quantity > free_space:
            raise NoFreeSpace
        if title in self.items.keys():
            self.items[title] = self.items[title] + quantity
        else:
            self.items[title] = quantity
        return self.items

    def remove(self, title, quantity):
        items = self.get_items()
        current_quantity = items.get(title)
        if title not in self.items.keys():
            raise NothingToRemove
        if quantity > current_quantity:
            raise LowQuantityOfProduct
        elif quantity == current_quantity:
            del self.items[title]
        else:
            self.items[title] = current_quantity - quantity
        return self.items

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)
