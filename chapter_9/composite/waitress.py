

from abstract import MenuComponent


class Waitress:

    def __init__(self, all_menus: MenuComponent) -> None:
        self._all_menus = all_menus

    def print_menu(self) -> None:
        print(str(self._all_menus))
