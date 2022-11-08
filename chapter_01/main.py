from abstract import Duck
from fly_behavior import *
from quack_behavior import *
from duck import *


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
