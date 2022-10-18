from abstract import Pizza, PizzaIngredientFactory


# Concrete class
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
