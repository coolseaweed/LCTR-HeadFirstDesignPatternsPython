from abstract import PizzaStore
from ingredient_factory import NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory
from pizza import *


class NYPizzaStore(PizzaStore):

    def create_pizza(self, type) -> object:
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
