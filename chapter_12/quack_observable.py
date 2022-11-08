from abstract import *


class Observable(QuackObservable):

    def __init__(self, duck) -> None:
        self._observers = []
        self._duck = duck

    def register_observer(self, observer) -> None:
        self._observers.append(observer)

    def notify_observers(self) -> None:
        for obs in self._observers:
            obs.update(self._duck)

    def get_observers(self):
        return self._observers
