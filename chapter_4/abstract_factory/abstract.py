from abc import ABCMeta, abstractmethod

# ingredient


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


# ingredient factory
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


# pizza
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


# pizza store
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
