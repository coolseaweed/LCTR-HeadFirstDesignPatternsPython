from abc import ABCMeta, abstractmethod
from enum import Enum


class Size(Enum):
    TALL = 1
    GRANDE = 2
    VENTI = 3


class Beverage(metaclass=ABCMeta):
    """ abstract class """

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
    """ abstract class """

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError

    def get_size(self) -> Size:
        return self.beverage.get_size()
