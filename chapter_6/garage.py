
from abstract import Command


class GarageDoor:
    """ Base class """

    def __init__(self, location: str = "") -> None:
        self._location = location

    def up(self) -> None:
        print(f"{self._location} garage Door is Up")

    def down(self) -> None:
        print(f"{self._location} garage Door is Down")

    def stop(self) -> None:
        print(f"{self._location} garage Door is Stopped")

    def light_on(self) -> None:
        print(f"{self._location} garage light is on")

    def light_off(self) -> None:
        print(f"{self._location} garage light is off")


# Concrete class
class GarageDoorUpCommand(Command):

    def __init__(self, garage_door) -> None:
        self._garage_door = garage_door

    def execute(self) -> None:
        self._garage_door.up()

    def undo(self) -> None:
        self._garage_door.down()


class GarageDoorDownCommand(Command):

    def __init__(self, garage_door) -> None:
        self._garage_door = garage_door

    def execute(self) -> None:
        self._garage_door.down()

    def undo(self) -> None:
        self._garage_door.up()
