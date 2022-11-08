from abstract import Command


class NoCommand(Command):
    """ null class """

    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass


class MacroCommand(Command):

    def __init__(self, commands: list) -> None:
        self._commands = commands

    def execute(self) -> None:
        for command in self._commands:
            command.execute()

    def undo(self) -> None:
        for command in reversed(self._commands):
            command.undo()
