from errors import BaseError
from request import Request
from shop import Shop
from storage import Storage
from store import Store

store = Store(
    items={"печеньки": 5,
           "вафли": 4,
           "шоколад": 6,
           "конфеты": 5,
           "темный шоколад": 3,
           "какао": 7},
    capacity=30
)

shop = Shop(
    items={"печеньки": 2,
           "конфеты": 5,
           "какао": 7}
)

storages: dict[str, Storage] = {"склад": store,
                                "магазин": shop}


def main():
    print("Добрый день\n")

    while True:
        print(f"На складе хранится:\n {store.get_items()}\n")
        print(f"В магазине хранится:\n {shop.get_items()}\n")
        user_input = input("Введите запрос в формате: 'Доставить 3 печеньки из склад в магазин'\n"
                           "или 'стоп'/'stop':\n")

        if user_input == 'стоп' or user_input == 'stop':
            break

        try:
            request = Request(user_input, storages)

            departure = storages.get(request.departure)
            destination = storages.get(request.destination)
            product = request.product
            amount = request.amount

            if product in departure.get_items():
                try:
                    departure.remove(title=product, quantity=amount)
                    print(f'Курьер забрал {amount} {product} со {request.departure}')
                    print(f'Курьер везет {amount} {product} со {request.departure} в {request.destination}')
                except BaseError as e:
                    print(e.message)
                    continue

                try:
                    destination.add(title=product, quantity=amount)
                    print(f'Курьер доставил {amount} {product} в {request.destination}')
                except BaseError as e:
                    print(e.message)
                    departure.add(title=product, quantity=amount)
                    continue
            else:
                print(f"{product} в {request.departure} отсутствует.")
        except BaseError as e:
            print(e.message)


if __name__ == '__main__':
    main()
