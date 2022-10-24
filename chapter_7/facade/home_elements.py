class Amplifier:

    def __init__(self, description) -> None:
        self._description = description
        self._tuner = None
        self._dvd_player = None
        self._cd_player = None

    def on(self) -> None:
        print(f"{self._description} on")

    def off(self) -> None:
        print(f"{self._description} off")

    def set_stereo_sound(self) -> None:
        print(f"{self._description} stereo mode on")

    def set_surround_sound(self) -> None:
        print(f"{self._description} surround sound on (5 speakers, 1 subwoofer)")

    def set_volume(self, level) -> None:
        print(f"{self._description}setting volume to {str(level)}")

    def set_tuner(self, tuner) -> None:
        print(f"{self._description} setting tuner to {tuner}")
        self._tuner = tuner

    def set_dvd(self, dvd) -> None:
        print(f"{self._description} setting DVD player to  {str(dvd)}")
        self._dvd_player = dvd

    def set_cd(self, cd) -> None:
        print(f"{self._description} setting CD player to {cd}")
        self._cd_player = cd

    def __str__(self):
        return self._description


class CDPlayer:

    def __init__(self, description, amplifier) -> None:
        self._description = description
        self._amplifier = amplifier
        self._current_track = None
        self._title = None

    def on(self) -> None:
        print(f"{self._description} on")

    def off(self) -> None:
        print(f"{self._description} off")

    def eject(self) -> None:
        self._title = None
        print(f"{self._description} eject")

    def play_title(self, title) -> None:
        self._title = title
        self._current_track = 0
        print(f"{self._description} playing {self._title}")

    def play_track(self, track) -> None:
        if self._title is None:
            print(
                f"{self._description} can't play track {self._current_track} no cd inserted")
        else:
            self._current_track = track
            print(f"{self._description} playing track {self._current_track}")

    def stop(self) -> None:
        self._current_track = 0
        print(f"{self._description} stopped")

    def pause(self) -> None:
        print(f"{self._description} paused {self._title}")

    def __str__(self):
        return self._description


class DvDPlayer:

    def __init__(self, description, amplifier) -> None:
        self._description = description
        self._amplifier = amplifier
        self._current_track = None
        self._movie = None

    def on(self) -> None:
        print(f"{self._description} on")

    def off(self) -> None:
        print(f"{self._description} off")

    def eject(self) -> None:
        print(f"{self._description} eject")

    def play_movie(self, movie) -> None:
        self._movie = movie
        self._current_track = 0
        print(f"{self._description} playing {self._movie}")

    def play_track(self, track) -> None:
        if self._movie is None:
            print(f"{self._description} can't play track {track} no dvd inserted")
        else:
            self._current_track = track
            print(
                f"{self._description} playing track {self._current_track} of {self._movie} ")

    def stop(self) -> None:
        self._current_track = 0
        print(f"{self._description} stopped {self._movie} ")

    def pause(self) -> None:
        print(f"{self._description} paused {self._movie}")

    def set_two_channel_audio(self) -> None:
        print(f"{self._description} set two channel audio")

    def set_surround_audio(self) -> None:
        print(f"{self._description}set surround audio")

    def __str__(self):
        return self._description


class PopcornPopper:

    def __init__(self, description) -> None:
        self._description = description

    def on(self) -> None:
        print(f"{self._description} on")

    def off(self) -> None:
        print(f"{self._description} off")

    def pop(self) -> None:
        print(f"{self._description} popping popcorn!")

    def __str__(self):
        return self._description


class Projector:

    def __init__(self, description, dvd_player) -> None:
        self._description = description
        self._dvd_player = dvd_player

    def on(self) -> None:
        print(f"{self._description} on")

    def off(self) -> None:
        print(f"{self._description} off")

    def wide_screen_mode(self) -> None:
        print(f"{self._description} in widescreen mode (16x9 aspect ratio)")

    def tv_move(self) -> None:
        print(f"{self._description} in tv mode (4x3 aspect ratio)")

    def __str__(self):
        return self._description


class Screen:

    def __init__(self, description) -> None:
        self._description = description

    def up(self) -> None:
        print(f"{self._description} going up")

    def down(self) -> None:
        print(f"{self._description} going down")

    def __str__(self):
        return self._description


class TheaterLights:

    def __init__(self, description) -> None:
        self._description = description

    def on(self) -> None:
        print(f"{self._description} on")

    def off(self) -> None:
        print(f"{self._description} off")

    def dim(self, level) -> None:
        print(f"{self._description} dimming to {str(level)} %")

    def __str__(self):
        return self._description


class Tuner:

    def __init__(self, description, amplifier) -> None:
        self._description = description
        self._frequency = None
        self._amplifier = amplifier

    def on(self) -> None:
        print(f"{self._description} on")

    def off(self) -> None:
        print(f"{self._description} off")

    def set_frequency(self, frequency) -> None:
        print(f"{self._description} setting frequency to {frequency}")
        self._frequency = frequency

    def set_am(self) -> None:
        print(f"{self._description} setting AM mode")

    def set_fm(self) -> None:
        print(f"{self._description} setting FM mode")

    def __str__(self):
        return self._description
