from abc import ABCMeta, abstractmethod


# -------------------------------------
# Abstract classes
# -------------------------------------
class Observer(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def update(self) -> None:
        raise NotImplementedError


class DisplayElement(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError


class Subject(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def notify_observer(self) -> None:
        raise NotImplementedError
