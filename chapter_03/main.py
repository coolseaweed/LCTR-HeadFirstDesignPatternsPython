from abstract import Size
from beverage import *
from condiment_decorator import *


def main() -> None:
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


if __name__ == "__main__":

    main()
