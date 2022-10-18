
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
