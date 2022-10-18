from interface import Command


class Light:
    """ Base class """

    def __init__(self, location: str = "") -> None:
        self._location = location

    def on(self) -> None:
        print(f"{self._location} light is on")

    def off(self) -> None:
        print(f"{self._location} light is off")


# Concrete class
class LightOnCommand(Command):

    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.on()

    def undo(self) -> None:
        self._light.off()


class LightOffCommand(Command):

    def __init__(self, light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.off()

    def undo(self) -> None:
        self._light.on()


class LivingroomLightOnCommand(Command):

    def __init__(self, light) -> None:
        self._ligth = light

    def execute(self) -> None:
        self._light.on()

    def undo(self) -> None:
        self._light.off()


class LivingRoomLightOffCommand(Command):

    def __init__(self, light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.off()

    def undo(self) -> None:
        self._light.on()
