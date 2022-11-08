from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def update(self, duck):
        raise NotImplementedError


class QuackObservable(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def register_observer(self, observer: Observer):
        raise NotImplementedError

    @abstractmethod
    def notify_observers(self):
        raise NotImplementedError


class Quackable(QuackObservable, metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def quack(self):
        raise NotImplementedError


class AbstractDuckFactory(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def create_mallard_duck(self):
        raise NotImplementedError

    @abstractmethod
    def create_redhead_duck(self):
        raise NotImplementedError

    @abstractmethod
    def create_duck_call(self):
        raise NotImplementedError

    @abstractmethod
    def create_rubber_duck(self):
        raise NotImplementedError
