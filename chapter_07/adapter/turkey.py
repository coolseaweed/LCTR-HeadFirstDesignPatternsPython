from abstract import Turkey, Duck


class WildTurkey(Turkey):

    def gobble(self):
        print(f"Gobble gobble")

    def fly(self):
        print(f"I'm flying a short distance")


class TurkeyAdapter(Duck):
    def __init__(self, turkey) -> None:
        self._turkey = turkey

    def quack(self) -> None:
        self._turkey.gobble()

    def fly(self) -> None:
        for i in range(5):
            self._turkey.fly()
