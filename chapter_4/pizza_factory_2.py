from abc import ABCMeta, abstractmethod
from typing import Any

""" Different pizza stores """


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


# -------------------------------------
# Implement classes
# -------------------------------------

# NYStyle Pizza
class NYStyleCheesePizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "NY Style Sauce and Cheese Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")


class NYStylePepperoniPizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "NY Style Pepperoni Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")
        self._toppings.append("Sliced Pepperoni")
        self._toppings.append("Garlic")
        self._toppings.append("Onion")
        self._toppings.append("Mushrooms")
        self._toppings.append("Red Pepper")


class NYStyleClamPizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "NY Style Clam Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")
        self._toppings.append("Fresh Clams from Long Island Sound")


class NYStyleVeggiePizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "NY Style Veggie Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")
        self._toppings.append("Garlic")
        self._toppings.append("Onion")
        self._toppings.append("Mushrooms")
        self._toppings.append("Red Pepper")


# ChicagoStyle Pizza
class ChicagoStyleCheesePizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "Chicago Style Deep Dish Cheese Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"
        self._toppings.append("Shredded Mozzarella Cheese")

    def cut(self) -> None:
        print("- Cutting the pizza into square slices")


class ChicagoStylePepperoniPizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "Chicago Style Pepperoni Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"

        self._toppings.append("Shredded Mozzarella Cheese")
        self._toppings.append("Black Olives")
        self._toppings.append("Spinach")
        self._toppings.append("Eggplant")
        self._toppings.append("Sliced Pepperoni")

    def cut(self) -> None:
        print("- Cutting the pizza into square slices")


class ChicagoStyleClamPizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "Chicago Style Clam Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"

        self._toppings.append("Shredded Mozzarella Cheese")
        self._toppings.append("Frozen Clams from Chesapeake Bay")

    def cut(self) -> None:
        print("- Cutting the pizza into square slices")


class ChicagoStyleVeggiePizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "Chicago Deep Dish Veggie Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"

        self._toppings.append("Shredded Mozzarella Cheese")
        self._toppings.append("Black Olives")
        self._toppings.append("Spinach")
        self._toppings.append("Eggplant")

    def cut(self) -> None:
        print("- Cutting the pizza into square slices")


# Pizza Stores
class NYPizzaStore(PizzaStore):

    def create_pizza(self, type: str) -> Pizza:

        if type == "cheese":
            return NYStyleCheesePizza()

        elif type == "veggie":
            return NYStyleVeggiePizza()

        elif type == "clam":
            return NYStyleClamPizza()

        elif type == "pepperoni":
            return NYStylePepperoniPizza()

        else:
            return None


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, type) -> Pizza:
        if type == "cheese":
            return ChicagoStyleCheesePizza()

        elif type == "veggie":
            return ChicagoStyleVeggiePizza()

        elif type == "clam":
            return ChicagoStyleClamPizza()

        elif type == "pepperoni":
            return ChicagoStylePepperoniPizza()

        else:
            return None


if __name__ == "__main__":
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.order_pizza("cheese")
    print(f"Ethan ordered a [{pizza.get_name()}]\n{pizza}\n")

    pizza = chicagoStore.order_pizza("cheese")
    print(f"Joel ordered a [{pizza.get_name()}]\n{pizza}\n")

    pizza = nyStore.order_pizza("clam")
    print(f"Ethan ordered a [{pizza.get_name()}]\n{pizza}\n")

    pizza = chicagoStore.order_pizza("clam")
    print(f"Joel ordered a [{pizza.get_name()}]\n{pizza}\n")

    pizza = nyStore.order_pizza("pepperoni")
    print(f"Joel ordered a [{pizza.get_name()}]\n{pizza}\n")

    pizza = chicagoStore.order_pizza("pepperoni")
    print(f"Ethan ordered a [{pizza.get_name()}]\n{pizza}\n")

    pizza = nyStore.order_pizza("veggie")
    print(f"Joel ordered a [{pizza.get_name()}]\n{pizza}\n")
