from abc import ABCMeta, abstractmethod
from typing import Any

""" Abstract Factory Pattern """


# -------------------------------------
# Abstract classes
# -------------------------------------
# Ingredients
class Cheese(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class Clams(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class Dough(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class Pepperoni(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class Sauce(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class Veggie(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def __str__(self):
        raise NotImplementedError
# __________________________________________


class PizzaIngredientFactory(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def create_dough(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def create_sauce(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def create_cheese(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def create_veggies(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def create_pepperoni(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def create_clam(self) -> None:
        raise NotImplementedError


class Pizza(metaclass=ABCMeta):
    """ abstract class """

    def __init__(self) -> None:
        self._name = None
        self._dough = None
        self._sauce = None
        self._veggies = []
        self._cheese = None
        self._pepperoni = None
        self._clam = None

    @abstractmethod
    def prepare(self) -> None:
        raise NotImplementedError

    def get_name(self) -> str:
        return self._name

    def set_name(self, name) -> None:
        self._name = name

    def bake(self) -> None:
        print("- Bake for 25 minutes at 350")

    def cut(self) -> None:
        print("- Cutting the pizza into diagonal slices")

    def box(self) -> None:
        print("- Place pizza in official PizzaStore box")

    def __str__(self) -> str:
        result = f"---- {self._name} ----\n"

        if self._dough is not None:
            result += f"* Dough: {str(self._dough)} \n"

        if self._sauce is not None:
            result += f"* Sauce: {str(self._sauce)} \n"

        if self._cheese is not None:
            result += f"* Cheese: {str(self._cheese)} \n"

        if self._veggies is not None:
            veggie_list = [str(veggie) for veggie in self._veggies]
            result += f"* Veggies: {', '.join(veggie_list)} \n"

        if self._clam is not None:
            result += f"* clam: {str(self._clam)} \n"

        if self._pepperoni is not None:
            result += f"* pepperoni: {str(self._pepperoni)} \n"

        result += "--------------------------------"
        return result


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

# _____ NYStyle _____
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_veggies(self) -> list:
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clams:
        return FreshClams()


class NYPizzaStore(PizzaStore):

    def create_pizza(self, type):
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")

        elif type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")

        elif type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("New York Style Clam Pizza")

        elif type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("New York Style Pepperoni Pizza")

        return pizza
# _______________________


# _____ ChicagoStyle _____
class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self) -> Dough:
        return ThickCrustDough()

    def create_sauce(self) -> Sauce:
        return PlumTomatoSauce()

    def create_cheese(self) -> Cheese:
        return MozzarellaCheese()

    def create_veggies(self) -> Veggie:
        return [BlackOlives(), Spinach(), Eggplant()]

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clams:
        return FrozenClams()


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, type) -> Pizza:
        pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("Chicago Style Cheese Pizza")

        elif type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("Chicago Style Veggie Pizza")

        elif type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("Chicago Style Clam Pizza")

        elif type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("Chicago Style Pepperoni Pizza")

        return pizza
# _______________________


# _____ Ingredients _____
# Cheese
class MozzarellaCheese(Cheese):
    def __str__(self):
        return "Shredded Mozzarella"


class ParmesanCheese(Cheese):
    def __str__(self):
        return "Shredded Parmesan"


class ReggianoCheese(Cheese):
    def __str__(self):
        return "Reggiano Cheese"


# Clams
class FreshClams(Clams):
    def __str__(self):
        return "Fresh Clams from Long Island Sound"


class FrozenClams(Clams):
    def __str__(self):
        return "Frozen Clams from Chesapeake Bay"


# Dough
class ThickCrustDough(Dough):
    def __str__(self):
        return "Thick crust dough"


class ThinCrustDough(Dough):
    def __str__(self):
        return "Thin Crust Dough"


# Pepperoni
class SlicedPepperoni(Pepperoni):
    def __str__(self):
        return "Sliced Pepperoni"


# Sauce
class MarinaraSauce(Sauce):
    def __str__(self):
        return "Marinara Sauce"


class PlumTomatoSauce(Sauce):
    def __str__(self):
        return "Tomato sauce with plum tomatoes"


# Veggie
class BlackOlives(Veggie):
    def __str__(self):
        return "Black Olives"


class Eggplant(Veggie):
    def __str__(self):
        return "Eggplant"


class Garlic(Veggie):
    def __str__(self):
        return "Garlic"


class Mushroom(Veggie):
    def __str__(self):
        return "Mushrooms"


class Onion(Veggie):
    def __str__(self):
        return "Onion"


class RedPepper(Veggie):
    def __str__(self):
        return "Red Pepper"


class Spinach(Veggie):
    def __str__(self):
        return "Spinach"
# _________________


# _____ Pizza types _____

class CheesePizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        super().__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f"Perparing .. {self._name}")
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()


class ClamPizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        super().__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f"Perparing .. {self._name}")
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._clam = self._ingredient_factory.create_clam()


class PepperoniPizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        super().__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f"Perparing .. {self._name}")

        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._veggies = self._ingredient_factory.create_veggies()

        print(self._veggies[0], )
        self._pepperoni = self._ingredient_factory.create_pepperoni()


class VeggiePizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        super().__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f"Perparing .. {self._name}")
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._veggies = self._ingredient_factory.create_veggies()
# _________________


if __name__ == "__main__":
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.order_pizza("cheese")
    print(f"Ethan ordered a [{pizza.get_name()}]\n{str(pizza)}\n")

    pizza = chicagoStore.order_pizza("cheese")
    print(f"Joel ordered a [{pizza.get_name()}]\n{str(pizza)}\n")

    pizza = nyStore.order_pizza("clam")
    print(f"Ethan ordered a [{pizza.get_name()}]\n{str(pizza)}\n")

    pizza = chicagoStore.order_pizza("clam")
    print(f"Joel ordered a [{pizza.get_name()}]\n{str(pizza)}\n")

    pizza = nyStore.order_pizza("pepperoni")
    print(f"Joel ordered a [{pizza.get_name()}]\n{str(pizza)}\n")

    pizza = chicagoStore.order_pizza("pepperoni")
    print(f"Ethan ordered a [{pizza.get_name()}]\n{str(pizza)}\n")

    pizza = nyStore.order_pizza("veggie")
    print(f"Joel ordered a [{pizza.get_name()}]\n{str(pizza)}\n")
