from interface import Command
from garage import *
from light import *


class SimpleRemoteControl(object):

    def __init__(self) -> None:
        self._slot = None

    def set_command(self, command: Command) -> None:
        self._slot = command

    def button_was_pressed(self) -> None:
        self._slot.execute()


def main() -> None:
    remote_control = SimpleRemoteControl()
    light = Light()
    garage_door = GarageDoor()
    light_on = LightOnCommand(light)
    garage_open = GarageDoorUpCommand(garage_door)

    remote_control.set_command(light_on)
    remote_control.button_was_pressed()
    remote_control.set_command(garage_open)
    remote_control.button_was_pressed()


if __name__ == "__main__":
    main()
