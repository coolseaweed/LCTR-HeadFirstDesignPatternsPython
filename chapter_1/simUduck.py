from abc import ABCMeta, abstractmethod


# -------------------------------------
# Fly behavior class
# -------------------------------------
class FlyBehavior:

    __metaclass__ = ABCMeta

    @abstractmethod
    def fly(self) -> NotImplementedError:
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print(f"I'm flying!")


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self) -> None:
        print("I'm flying like a rocket!")

# -------------------------------------
# Quack behavior class
# -------------------------------------


class QuackBehavior:

    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self) -> NotImplementedError:
        raise NotImplementedError


class Quack(QuackBehavior):
    def quack(self) -> None:
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self) -> None:
        print("<< silence ~ >>")


class Squeak(QuackBehavior):
    def quack(self) -> None:
        print("Sqeak")


class FakeQuack(QuackBehavior):
    def quack(self) -> None:
        print("Qwak")


# -------------------------------------
# Duck class
# -------------------------------------


class Duck:

    __metaclass__ = ABCMeta

    def __init__(self) -> None:
        self.quack_behavior = None
        self.fly_behavior = None

    def perform_fly(self) -> None:
        self.fly_behavior.fly()

    def perform_quack(self) -> None:
        self.quack_behavior.quack()

    def set_fly_behavior(self, fly_behavior: FlyBehavior) -> None:
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior) -> None:
        self.quack_behavior = quack_behavior

    @abstractmethod
    def display(self) -> NotImplementedError:
        raise NotImplementedError

    def swim(self) -> None:
        print("All ducks float, even decoys!")


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


# -------------------------------------
# MAIN
# -------------------------------------
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
