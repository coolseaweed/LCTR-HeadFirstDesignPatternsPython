from abc import ABCMeta, abstractmethod


class FlyBehavior(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def fly(self) -> NotImplementedError:
        raise NotImplementedError


class QuackBehavior(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def quack(self) -> NotImplementedError:
        raise NotImplementedError


class Duck(metaclass=ABCMeta):
    """ abstract class """

    def __init__(self) -> None:
        self.quack_behavior = None
        self.fly_behavior = None

    def perform_fly(self) -> None:
        self.fly_behavior.fly()

    def perform_quack(self) -> None:
        self.quack_behavior.quack()

    def set_fly_behavior(self, fly_behavior: FlyBehavior) -> None:
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior) -> None:
        self.quack_behavior = quack_behavior

    @abstractmethod
    def display(self) -> NotImplementedError:
        raise NotImplementedError

    def swim(self) -> None:
        print("All ducks float, even decoys!")
