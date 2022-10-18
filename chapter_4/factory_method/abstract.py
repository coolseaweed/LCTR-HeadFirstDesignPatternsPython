from abc import ABCMeta, abstractmethod


# -------------------------------------
# Abstract classes
# -------------------------------------
class Pizza(metaclass=ABCMeta):
    """ abstract class """

    @abstractmethod
    def __init__(self) -> None:
        self._name = None
        self._dough = None
        self._sauce = None
        self._toppings = []

    def __str__(self) -> str:
        display = ""
        display += f"---- {self._name} ----\n"
        display += f"* {self._dough}\n"
        display += f"* {self._sauce}\n* "
        display += "\n* ".join(self._toppings)
        display += f"\n--------------------------\n"

        return display

    def get_name(self) -> str:
        return self._name

    def prepare(self) -> None:
        print("Preparing " + self._name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        print(" ".join(self._toppings))

    def bake(self) -> None:
        print("- Bake for 25 minutes at 350")

    def cut(self) -> None:
        print("- Cutting the pizza into diagonal slices")

    def box(self) -> None:
        print("- Place pizza in official PizzaStore box")


class PizzaStore(metaclass=ABCMeta):
    """ abstract class """

    def order_pizza(self, type: str) -> Pizza:
        pizza = self.create_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, type: str) -> Pizza:
        raise NotImplementedError
