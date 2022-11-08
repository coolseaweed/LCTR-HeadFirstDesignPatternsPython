from menu import CafeMenu, DinerMenu


class Waitress:
    def __init__(
        self,
        cafe_menu: CafeMenu,
        diner_menu: DinerMenu
    ) -> None:

        self.cafe_menu = cafe_menu
        self.diner_menu = diner_menu

    def _print_menu(self, iter_menu) -> None:
        for menu_item in iter_menu:
            print(f"{menu_item.name}, {menu_item.price} -- {menu_item.description}")

    def print_menu(self) -> None:
        print("MENU\n----\nBREAKFAST")
        print("not implemented")
        print("\nLUNCH")
        self._print_menu(self.cafe_menu)
        print("\nDINNER")
        self._print_menu(self.diner_menu)

    def _is_vegetarian(self, name, iter_menu):
        for menu_item in iter_menu:
            if menu_item.name == name:
                return menu_item.vegetarian
        return False

    def is_item_vegetarian(self, name) -> bool:
        if self._is_vegetarian(name, self.cafe_menu):
            return True
        if self._is_vegetarian(name, self.diner_menu):
            return True
        return False
