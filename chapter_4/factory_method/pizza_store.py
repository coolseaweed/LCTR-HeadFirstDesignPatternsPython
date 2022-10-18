from abstract import PizzaStore, Pizza
from pizza import *


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
