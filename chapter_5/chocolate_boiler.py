from singleton import Singleton, SingletonError


class ChocolateBoiler(metaclass=Singleton):
    def __init__(self) -> None:
        self.empty = True
        self.boiled = False

    def fill(self) -> None:
        if not self.empty:
            raise SingletonError
        self.empty = False
        self.boiled = False
        print("Full!")

    def drain(self) -> None:
        if self.empty or (not self.boiled):
            raise SingletonError
        self.empty = True
        print("Empty!")

    def boil(self) -> None:
        self.boiled = True
        print("boiled!")

    def is_empty(self) -> bool:
        return self.empty

    def is_boiled(self) -> bool:
        return self.boiled
