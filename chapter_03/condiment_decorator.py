from abstract import CondimentDecorator


# Concrete Class
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
