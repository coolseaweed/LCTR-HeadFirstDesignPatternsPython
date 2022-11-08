from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def insert_quarter(self):
        raise NotImplementedError

    @abstractmethod
    def eject_quarter(self):
        raise NotImplementedError

    @abstractmethod
    def turn_crank(self):
        raise NotImplementedError

    @abstractmethod
    def dispense(self):
        raise NotImplementedError


class GumballMachineRemote(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def get_count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_location(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_state(self) -> State:
        raise NotImplementedError
