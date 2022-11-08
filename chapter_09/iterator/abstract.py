from abc import ABCMeta, abstractmethod


class Menu(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def __iter__(self):
        raise NotImplementedError
