from abstract import Command


class TV:
    """ Base class """

    def __init__(self, location: str = "") -> None:
        self._location = location
        self._channel = 0

    def on(self) -> None:
        print("TV is on")

    def off(self) -> None:
        print("TV is off")

    def set_input_channel(self) -> None:
        self._channel = 3
        print("Channell is set for VCR")


class TVOffCommand(Command):

    def __init__(self, tv) -> None:
        self._tv = tv

    def execute(self) -> None:
        self._tv.off()

    def undo(self) -> None:
        self._tv.on()


class TVOnCommand(Command):

    def __init__(self, tv) -> None:
        self._tv = tv

    def execute(self) -> None:
        self._tv.on()

    def undo(self) -> None:
        self._tv.off()
