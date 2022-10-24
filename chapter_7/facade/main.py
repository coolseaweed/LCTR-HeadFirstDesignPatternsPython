from home_theather import HomeTheatherFacade
from home_elements import *


def main() -> None:
    # Home Theater Test Drive
    AMP = Amplifier("Top-O-Line Amplifier")
    TUNER = Tuner("Top-O-Line AM/FM Tuner", AMP)
    DVD = DvDPlayer("Top-O-Line DVD Player", AMP)
    CD = CDPlayer("Top-O-Line CD Player", AMP)
    PROJECTOR = Projector("Top-O-Line Projector", DVD)
    LIGHTS = TheaterLights("Theater Ceiling Lights")
    SCREEN = Screen("Theater Screen")
    POPPER = PopcornPopper("Popcorn Popper")

    HOME_THEATER = HomeTheatherFacade(
        AMP, TUNER, DVD, CD, PROJECTOR, SCREEN,
        LIGHTS, POPPER)

    HOME_THEATER.watch_movie("Raiders of the Lost Ark")
    HOME_THEATER.end_movie()


if __name__ == "__main__":
    main()
