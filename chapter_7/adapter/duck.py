from abstract import Duck, Turkey
import random


class MallarDuck(Duck):
    def quack(self) -> None:
        print(f"Quack")

    def fly(self) -> None:
        print(f"I'm flying")


class DuckAdapter(Turkey):
    def __init__(self, duck) -> None:
        self._duck = duck

    def gobble(self) -> None:
        self._duck.quack()

    def fly(self) -> None:
        if random.randint(0, 5) == 0:
            self._duck.fly()
