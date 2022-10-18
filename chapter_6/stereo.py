from interface import Command


class Stereo:
    """ Base class """

    def __init__(self, location: str = "") -> None:
        self._location = location

    def on(self) -> None:
        print(f"{self._location} stereo is on")

    def off(self) -> None:
        print(f"{self._location} stereo is off")

    def set_cd(self) -> None:
        print(f"{self._location} stereo is set for CD input")

    def set_dvd(self) -> None:
        print(f"{self._location} stereo is set for Radio")

    def set_volume(self, volume) -> None:
        print(f"{self._location} Stereo volume set to {str(volume)}")


# Concrete class
class StereoOnWithCDCommand(Command):

    def __init__(self, stereo) -> None:
        self._stereo = stereo

    def execute(self) -> None:
        self._stereo.on()
        self._stereo.set_cd()
        self._stereo.set_volume(11)

    def undo(self) -> None:
        self._light.off()


class StereoOffCommand(Command):

    def __init__(self, stereo) -> None:
        self._stereo = stereo

    def execute(self) -> None:
        self._stereo.off()

    def undo(self) -> None:
        self._stereo.on()
        self._stereo.set_cd()
        self._stereo.set_volume(11)
