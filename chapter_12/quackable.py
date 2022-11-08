from abstract import *
from quack_observable import Observable


class QuackCounter(Quackable):
    """ decorater pattern """

    number_of_quacks = 0

    def __init__(self, duck) -> None:
        self._duck = duck

    def quack(self) -> None:
        self._duck.quack()
        QuackCounter.number_of_quacks += 1

    @staticmethod
    def get_quacks() -> int:
        return QuackCounter.number_of_quacks

    def register_observer(self, observer) -> None:
        self._duck.register_observer(observer)

    def notify_observers(self) -> None:
        self._duck.notify_observers()

    def __str__(self) -> str:
        return str(self._duck)


class Goose:

    def honk(self) -> None:
        print("Honk")

    def __str__(self):
        return "Goose"


class GooseAdapter(Quackable):
    """ adapter pattern """

    def __init__(self, goose) -> None:
        self._goose = goose
        self._observable = Observable(self)

    def quack(self) -> None:
        self._goose.honk()
        self.notify_observers()

    def register_observer(self, observer) -> None:
        self._observable.register_observer(observer)

    def notify_observers(self) -> None:
        self._observable.notify_observers()

    def __str__(self):
        return "Goose pretending to be a Duck"


class DecoyDuck(Quackable):

    def __init__(self) -> None:
        self._observable = Observable(self)

    def quack(self) -> None:
        print("<< Silence >>")
        self.notify_observers()

    def register_observer(self, observer) -> None:
        self._observable.register_observer(observer)

    def notify_observers(self) -> None:
        self._observable.notify_observers()

    def __str__(self):
        return "Decoy Duck"


class DuckCall(Quackable):

    def __init__(self) -> None:
        self._observable = Observable(self)

    def quack(self) -> None:
        print("Kwak")
        self.notify_observers()

    def register_observer(self, observer) -> None:
        self._observable.register_observer(observer)

    def notify_observers(self) -> None:
        self._observable.notify_observers()

    def __str__(self):
        return "Duck Call"


class MallardDuck(Quackable):

    def __init__(self) -> None:
        self._observable = Observable(self)

    def quack(self) -> None:
        print("Quack")
        self.notify_observers()

    def register_observer(self, observer) -> None:
        self._observable.register_observer(observer)

    def notify_observers(self) -> None:
        self._observable.notify_observers()

    def __str__(self):
        return "Mallard Duck"


class RedheadDuck(Quackable):

    def __init__(self) -> None:
        self._observable = Observable(self)

    def quack(self) -> None:
        print("Quack")
        self.notify_observers()

    def register_observer(self, observer) -> None:
        self._observable.register_observer(observer)

    def notify_observers(self) -> None:
        self._observable.notify_observers()

    def __str__(self):
        return "Redhead Duck"


class RubberDuck(Quackable):

    def __init__(self) -> None:
        self._observable = Observable(self)

    def quack(self) -> None:
        print("Squeak")
        self.notify_observers()

    def register_observer(self, observer) -> None:
        self._observable.register_observer(observer)

    def notify_observers(self) -> None:
        self._observable.notify_observers()

    def __str__(self):
        return "Rubber Duck"


class Flock(Quackable):
    """ combining pattern """

    def __init__(self):
        self._ducks = []

    def add(self, duck):
        self._ducks.append(duck)

    def quack(self):
        for duck in self._ducks:
            duck.quack()

    def register_observer(self, observer):
        for duck in self._ducks:
            duck.register_observer(observer)

    def notify_observers():
        pass

    def __str__(self):
        return "Flock of Ducks"
