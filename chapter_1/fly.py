from abstract import FlyBehavior


# Concrete class
class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print(f"I'm flying!")


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self) -> None:
        print("I'm flying like a rocket!")
