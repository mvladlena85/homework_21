from errors import WrongRequest
from storage import Storage


class Request:
    def __init__(self, request: str, storages: dict[str: Storage]):
        split_request: list = request.split(" ")

        if len(split_request) != 7:
            raise WrongRequest("Запрос не соответствует указанному формату")

        self.departure = split_request[4]
        self.destination = split_request[6]
        self.amount = int(split_request[1])
        self.product = split_request[2]

        if self.departure not in storages or self.destination not in storages:
            raise WrongRequest("Проверьте правильность написания пунктов отправления/назначения")


    # @property
    # def departure(self):
    #     return self.departure


