from abstract import QuackBehavior


# Concrete class
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
