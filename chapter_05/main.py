
from chocolate_boiler import ChocolateBoiler


def main() -> None:
    boiler = ChocolateBoiler()
    boiler.fill()
    boiler.boil()
    boiler2 = ChocolateBoiler()
    boiler.drain()
    print(boiler2 is boiler)


if __name__ == "__main__":
    main()
