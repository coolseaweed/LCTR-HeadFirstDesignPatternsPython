
from abstract import Command


class CeilingFan:
    """ Base class """

    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    def __init__(self, location: str = "") -> None:
        self._location = location
        self._speed = CeilingFan.OFF

    def high(self) -> None:
        self._speed = CeilingFan.HIGH
        print(f"{self._location} ceiling fan is on high")

    def medium(self) -> None:
        self._speed = CeilingFan.MEDIUM
        print(f"{self._location} ceiling fan is on medium")

    def low(self) -> None:
        self._speed = CeilingFan.LOW
        print(f"{self._location} ceiling fan is on low")

    def off(self) -> None:
        self._speed = CeilingFan.OFF
        print(f"{self._location} ceiling fan is off")

    def get_speed(self) -> int:
        return self._speed


# Concrete class
class CeilingFanHighCommand(Command):

    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self._ceiling_fan = ceiling_fan

    def execute(self) -> None:
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.high()

    def undo(self) -> None:
        if self._prev_speed == CeilingFan.HIGH:
            self._ceiling_fan.high()
        elif self._prev_speed == CeilingFan.MEDIUM:
            self._ceiling_fan.medium()
        elif self._prev_speed == CeilingFan.LOW:
            self._ceiling_fan.low()
        elif self._prev_speed == CeilingFan.OFF:
            self._ceiling_fan.off()
        else:
            raise ValueError(f"unknown value: { self._prev_speed}")


class CeilingFanMediumCommand(Command):

    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self._ceiling_fan = ceiling_fan

    def execute(self) -> None:
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.medium()

    def undo(self) -> None:
        if self._prev_speed == CeilingFan.HIGH:
            self._ceiling_fan.high()
        elif self._prev_speed == CeilingFan.MEDIUM:
            self._ceiling_fan.medium()
        elif self._prev_speed == CeilingFan.LOW:
            self._ceiling_fan.low()
        elif self._prev_speed == CeilingFan.OFF:
            self._ceiling_fan.off()
        else:
            raise ValueError(f"unknown value: { self._prev_speed}")


class CeilingFanLowCommand(Command):

    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self._ceiling_fan = ceiling_fan

    def execute(self) -> None:
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.low()

    def undo(self) -> None:
        if self._prev_speed == CeilingFan.HIGH:
            self._ceiling_fan.high()
        elif self._prev_speed == CeilingFan.MEDIUM:
            self._ceiling_fan.medium()
        elif self._prev_speed == CeilingFan.LOW:
            self._ceiling_fan.low()
        elif self._prev_speed == CeilingFan.OFF:
            self._ceiling_fan.off()
        else:
            raise ValueError(f"unknown value: { self._prev_speed}")


class CeilingFanOffCommand(Command):

    def __init__(self, ceiling_fan) -> None:
        self._ceiling_fan = ceiling_fan

    def execute(self) -> None:
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.off()

    def undo(self) -> None:
        if self._prev_speed == CeilingFan.HIGH:
            self._ceiling_fan.high()
        elif self._prev_speed == CeilingFan.MEDIUM:
            self._ceiling_fan.medium()
        elif self._prev_speed == CeilingFan.LOW:
            self._ceiling_fan.low()
        elif self._prev_speed == CeilingFan.OFF:
            self._ceiling_fan.off()
        else:
            raise ValueError(f"unknown value: {self._prev_speed}")
