from abc import ABCMeta, abstractmethod
from enum import Enum


class Size(Enum):
    TALL = 1
    GRANDE = 2
    VENTI = 3


# -------------------------------------
# Abstract classes
# -------------------------------------
class Beverage:

    __metaclass__ = ABCMeta

    def __init__(self) -> None:
        self.description = "Unknown Beverage"
        self.size = Size.TALL

    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError

    def set_size(self, size: Size) -> None:
        self.size = size

    def get_size(self) -> Size:
        return self.size.name


class CondimentDecorator(Beverage):

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError

    def get_size(self) -> Size:
        return self.beverage.get_size()


# -------------------------------------
# Implement classes
# -------------------------------------

# Beverage
class Espresso(Beverage):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self) -> None:
        super().__init__()
        self.description = "House Blend Coffee"

    def cost(self) -> float:
        return 0.89


class Decaf(Beverage):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Decaf"

    def cost(self) -> float:
        return 1.05


class DarkRoast(Beverage):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Dark Roast"

    def cost(self) -> float:
        return 0.99


# CondimentDecorator
class Mocha(CondimentDecorator):

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return 0.20 + self.beverage.cost()


class Soy(CondimentDecorator):

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Soy"

    def cost(self) -> float:
        return 0.15 + self.beverage.cost()


class Whip(CondimentDecorator):

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return 0.10 + self.beverage.cost()


class SteamedMilk(CondimentDecorator):

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Steamed Milk"

    def cost(self) -> float:
        return 0.10 + self.beverage.cost()


if __name__ == "__main__":

    bever_1 = Espresso()
    print(
        f"bever 1: {bever_1.get_description()}, cost: {bever_1.cost()} $, size: {bever_1.get_size()}")

    bever_2 = DarkRoast()
    bever_2.set_size(Size.GRANDE)
    bever_2 = Mocha(bever_2)
    bever_2 = Mocha(bever_2)
    bever_2 = Whip(bever_2)
    print(
        f"bever 2: {bever_2.get_description()}, cost: {bever_2.cost()} $, size: {bever_2.get_size()}")

    bever_3 = HouseBlend()
    bever_3.set_size(Size.VENTI)
    bever_3 = Soy(bever_3)
    bever_3 = Mocha(bever_3)
    bever_3 = Whip(bever_3)
    print(
        f"bever 3: {bever_3.get_description()}, cost: {bever_3.cost()} $, size: {bever_3.get_size()}")
