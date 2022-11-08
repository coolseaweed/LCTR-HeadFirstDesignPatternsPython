from abstract import Command
from command import NoCommand


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


class SimpleRemoteControl(object):

    def __init__(self) -> None:
        self._slot = None

    def set_command(self, command: Command) -> None:
        self._slot = command

    def button_was_pressed(self) -> None:
        self._slot.execute()
