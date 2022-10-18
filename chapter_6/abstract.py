from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def execute(self):
        raise NotImplementedError

    @abstractmethod
    def undo(self):
        raise NotImplementedError
