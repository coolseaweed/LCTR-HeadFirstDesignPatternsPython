from abc import ABCMeta, abstractmethod

""" Simple Factory Pattern """

# -------------------------------------
# Abstract classes
# -------------------------------------


class Pizza(metaclass=ABCMeta):
    """ abstract class """

    @abstractmethod
    def __init__(self) -> None:
        pass

    def get_name(self) -> str:
        return self._name

    def prepare(self) -> None:
        print("Preparing " + self._name)

    def bake(self) -> None:
        print("Baking " + self._name)

    def cut(self) -> None:
        print("Cutting " + self._name)

    def box(self) -> None:
        print("Boxing " + self._name)


# -------------------------------------
# Implement classes
# -------------------------------------
class SimplePizzaFactory:

    def create_pizza(self, pizza_type) -> None:
        pizza = None

        if pizza_type == 'cheese':
            pizza = CheesePizza()

        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza()

        elif pizza_type == "clam":
            pizza = ClamPizza()

        elif pizza_type == "veggie":
            pizza = VeggiePizza()

        return pizza


class PizzaStore:

    def __init__(self, factory: SimplePizzaFactory) -> None:
        self._factory = factory

    def order_pizza(self, pizza_type) -> Pizza:
        pizza = self._factory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class CheesePizza(Pizza):

    def __init__(self) -> None:
        self._name = "Cheese Pizza"
        self._dough = "Regular Crust"
        self._sauce = "Marinara Pizza Sauce"
        self._toppings = []
        self._toppings.append("Fresh Mozzarella")
        self._toppings.append("Parmesan")


class PepperoniPizza(Pizza):

    def __init__(self) -> None:
        self._name = "Pepperoni Pizza"
        self._dough = "Crust"
        self._sauce = "Marinara sauce"
        self._toppings = []
        self._toppings.append("Sliced Pepperoni")
        self._toppings.append("Sliced Onion")
        self._toppings.append("Grated parmesan cheese")


class ClamPizza(Pizza):

    def __init__(self) -> None:
        self._name = "Clam Pizza"
        self._dough = "Thin crust"
        self._sauce = "White garlic sauce"
        self._toppings = []
        self._toppings.append("Clams")
        self._toppings.append("Grated parmesan cheese")


class VeggiePizza(Pizza):

    def __init__(self) -> None:
        self._name = "Veggie Pizza"
        self._dough = "Crust"
        self._sauce = "Marinara sauce"
        self._toppings = []
        self._toppings.append("Shredded mozzarella")
        self._toppings.append("Grated parmesan")
        self._toppings.append("Diced onion")
        self._toppings.append("Sliced mushrooms")
        self._toppings.append("Sliced red pepper")
        self._toppings.append("Sliced black olives")


if __name__ == "__main__":
    factory = SimplePizzaFactory()
    store = PizzaStore(factory)

    pizza = store.order_pizza("cheese")
    print(f"We order a {pizza.get_name()}\n")

    pizza = store.order_pizza("veggie")
    print(f"We order a {pizza.get_name()}\n")
