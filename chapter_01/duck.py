from abstract import Duck
from fly_behavior import FlyWithWings, FlyNoWay
from quack_behavior import Quack


class MallarDuck(Duck):
    def __init__(self) -> None:
        super().__init__()
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self) -> None:
        print(f"I'm a real Mallard duck")


class ModelDuck(Duck):
    def __init__(self) -> None:
        super().__init__()
        self.quack_behavior = Quack()
        self.fly_behavior = FlyNoWay()

    def display(self) -> None:
        print(f"I'm a Model Duck")
