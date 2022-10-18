from interface import Command
from ceiling import *
from garage import *
from tv import *
from hottub import *
from light import *
from stereo import *


class NoCommand(Command):
    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass


class RemoteControl(object):
    def __init__(self, num_cmds: int = 7) -> None:
        self._on_commands = [NoCommand()] * num_cmds
        self._off_commands = [NoCommand()] * num_cmds
        self._undo_command = NoCommand()

        assert len(self._on_commands) == len(self._off_commands)

    def set_command(self, slot: int, on_command: Command, off_command: Command) -> None:
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int) -> None:
        self._on_commands[slot].execute()
        self._undo_command = self._on_commands[slot]

    def off_button_was_pushed(self, slot: int) -> None:
        self._off_commands[slot].execute()
        self._undo_command = self._off_commands[slot]

    def undo_button_was_pushed(self) -> None:
        self._undo_command.undo()

    def __str__(self) -> str:
        string_buff = "\n------ Remote Control Info. -------\n"
        for slot in range(len(self._on_commands)):
            on_command = self._on_commands[slot]
            off_command = self._off_commands[slot]

            string_buff += f"[slot {str(slot)}] {  on_command.__class__.__name__}\t{off_command.__class__.__name__}\n"
        string_buff += f"[undo] {self._undo_command.__class__.__name__}\n"
        string_buff += "------------------------------------\n"

        return string_buff


def main() -> None:
    remote_control = RemoteControl()
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    ceiling_fan = CeilingFan("Living Room")
    garage_door = GarageDoor("")
    stereo = Stereo("Living Room")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_med = CeilingFanMediumCommand(ceiling_fan)
    ceiling_fan_low = CeilingFanLowCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

    garage_door_up = GarageDoorUpCommand(garage_door)
    garage_door_down = GarageDoorDownCommand(garage_door)

    stereo_on_with_cd = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, ceiling_fan_med, ceiling_fan_off)
    remote_control.set_command(3, ceiling_fan_high, ceiling_fan_off)
    remote_control.set_command(4, stereo_on_with_cd, stereo_off)

    print(f"[slot 0] test ----")
    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    print(str(remote_control))

    remote_control.undo_button_was_pushed()

    print(f"\n[slot 1] test ----")
    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)

    print(f"\n[slot 2] test ----")
    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)
    print(str(remote_control))
    remote_control.undo_button_was_pushed()

    print(f"\n[slot 3] test ----")
    remote_control.on_button_was_pushed(3)
    print(str(remote_control))
    remote_control.undo_button_was_pushed()

    print(f"\n[slot 4] test ----")
    remote_control.on_button_was_pushed(4)
    remote_control.off_button_was_pushed(4)
    remote_control.undo_button_was_pushed()
    remote_control.undo_button_was_pushed()


if __name__ == "__main__":
    main()
