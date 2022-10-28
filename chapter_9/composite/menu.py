from io import UnsupportedOperation
from abstract import MenuComponent


class MenuItem(MenuComponent):

    def __init__(self, name, description, vegetarian, price) -> None:
        self._name = name
        self._description = description
        self._vegetarian = vegetarian
        self._price = price

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price

    def is_vegetarian(self):
        return self._vegetarian

    def __str__(self) -> str:
        result = f"\n {self._name}"
        if self._vegetarian is True:
            result += "(v)"
        result += f", {str(self._price)}\n"
        result += f"     -- {self._description}\n"
        return result


class Menu(MenuComponent):

    def __init__(self, name, description) -> None:
        self._name = name
        self._description = description
        self._menu_components = []

    def add(self, menu_component: MenuComponent) -> None:
        self._menu_components.append(menu_component)

    def remove(self, menu_component: MenuComponent) -> None:
        self._menu_components.remove(menu_component)

    def get_child(self, i):
        return self._menu_components[i]

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def __str__(self):
        result = f"\n{self._name}"
        result += f", {self._description}\n"
        result += "---------------------\n"
        result += ''.join([str(menu) for menu in self._menu_components])
        return result
