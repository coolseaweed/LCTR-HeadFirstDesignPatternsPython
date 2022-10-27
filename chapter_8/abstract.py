from abc import ABCMeta, abstractmethod


class CaffeinBeverage(metaclass=ABCMeta):
    """ abstract class """

    def prepare_recipe(self) -> None:
        """ template method """
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew(self):
        raise NotImplementedError

    @abstractmethod
    def add_condiments(self):
        raise NotImplementedError

    def boil_water(self) -> None:
        print(f"Boiling water")

    def pour_in_cup(self) -> None:
        print(f"pouring into cup")


class CaffeineBeverageWithHook(metaclass=ABCMeta):
    """ abstract class """

    def prepare_recipe(self) -> None:
        """ template method """
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    @abstractmethod
    def brew(self):
        raise NotImplementedError

    @abstractmethod
    def add_condiments(self):
        raise NotImplementedError

    def boil_water(self) -> None:
        print(f"Boiling water")

    def pour_in_cup(self) -> None:
        print(f"pouring into cup")

    def customer_wants_condiments(self) -> bool:
        return True
