from abstract import Menu


class MenuItem:
    def __init__(
        self,
        name: str,
        description: str,
        vegetarian: bool,
        price: float,
    ) -> None:

        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price


class DinerMenu(Menu):
    """ iterator is list type """

    def __init__(self) -> None:
        self.menu_items = []

    def add_item(
        self,
        name: str,
        description: str,
        vegetarian: bool,
        price: float,
    ) -> None:

        self.menu_items.append(
            MenuItem(name, description, vegetarian, price)
        )

    def __iter__(self):
        return iter(self.menu_items)


class CafeMenu(Menu):
    def __init__(self) -> None:
        self.menu_items = {}

    def add_item(
        self,
        name: str,
        description: str,
        vegetarian: bool,
        price: float,
    ) -> None:
        self.menu_items[name] = MenuItem(name, description, vegetarian, price)

    def __iter__(self):
        return iter(self.menu_items.values())
