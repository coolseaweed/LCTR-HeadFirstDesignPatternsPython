from abstract import Beverage


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
