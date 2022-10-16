class SingletonError(Exception):
    pass


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


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

    def boil(self):
        self.boiled = True
        print("boiled!")

    def is_empty(self) -> bool:
        return self.empty

    def is_boiled(self) -> bool:
        return self.boiled


def main() -> None:
    boiler = ChocolateBoiler()
    boiler.fill()
    boiler.boil()
    boiler2 = ChocolateBoiler()
    boiler.drain()
    print(boiler2 is boiler)


if __name__ == "__main__":
    main()
