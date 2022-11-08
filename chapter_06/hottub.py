from abstract import Command


class Hottub:
    """ Base class"""

    def __init__(self) -> None:
        self._on = False
        self._temperature = 0

    def on(self) -> None:
        self._on = True

    def off(self) -> None:
        self._off = False

    def bubbles_on(self) -> None:
        if self._on is True:
            print("Hottub is bubbling!")

    def bubbles_off(self) -> None:
        if self._on is True:
            print("Hottub is not bubbling!")

    def jets_on(self) -> None:
        if self._on is True:
            print("Hottub jets are on")

    def jets_off(self) -> None:
        if self._on is True:
            print("Hottub jets are off")

    def set_temperature(self, temperature) -> None:
        self._temperature = temperature

    def heat(self) -> None:
        self._temperature = 105
        print("Hottub is heating to a steaming 105 degrees")

    def cool(self) -> None:
        self._temperature = 98
        print("Hottub is cooling to 98 degrees")


# Concrete class
class HottubOnCommand(Command):

    def __init__(self, hottub: Hottub) -> None:
        self._hottub = hottub

    def execute(self) -> None:
        self._hottub.on()
        self._hottub.heat()
        self._hottub.bubbles_on()

    def undo(self) -> None:
        self._hottub.cool()
        self._hottub.off()


class HottubOffCommand(Command):

    def __init__(self, hottub) -> None:
        self._hottub = hottub

    def execute(self) -> None:
        self._hottub.cool()
        self._hottub.off()

    def undo(self) -> None:
        self._hottub.on()
        self._hottub.heat()
        self._hottub.bubbles_on()
