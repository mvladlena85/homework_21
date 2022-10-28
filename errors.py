class BaseError(Exception):
    def __init__(self, message=None):
        self.message = f"Что-то пошло не так."
        super(BaseError, self).__init__(self.message)


class NoFreeSpace(BaseError):
    def __init__(self):
        self.message = f"Недостаточно места, попробуйте что-то другое."


class FullRangeOfGoods(BaseError):
    def __init__(self):
        self.message = f"Превышено количество позиций в магазине."


class NothingToRemove(BaseError):
    def __init__(self):
        self.message = f"Такого продукта нет."

    # def __str__(self):
    #     return self.message


class WrongRequest(BaseError):
    def __init__(self, message):
        self.message = message


class LowQuantityOfProduct(BaseError):
    def __init__(self):
        self.message = f"Не хватает на складе, попробуйте заказать меньше."
