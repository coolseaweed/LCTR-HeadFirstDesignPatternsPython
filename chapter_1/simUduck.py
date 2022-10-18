from abstract import Duck
from fly import *
from quack import *


# Duck
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


# main
if __name__ == "__main__":

    print(f"<< Mallar Duck TEST >>")
    mallar_duck = MallarDuck()
    mallar_duck.perform_quack()
    mallar_duck.perform_fly()
    mallar_duck.display()
    print(f"----------------------------------")
    print(f"<< Model Duck TEST >>")
    model_duck = ModelDuck()
    model_duck.perform_fly()
    model_duck.set_fly_behavior(FlyRocketPowered())
    model_duck.perform_fly()
