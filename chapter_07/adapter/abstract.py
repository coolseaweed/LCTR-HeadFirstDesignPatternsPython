from abc import ABCMeta, abstractmethod


class Duck(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def quack(self):
        raise NotImplementedError

    @abstractmethod
    def fly(self):
        raise NotADirectoryError


class Turkey(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def gobble(self):
        raise NotImplementedError

    @abstractmethod
    def fly(self):
        raise NotImplementedError
