from abstract import GumballMachineRemote
from state import *
import json
import pickle
import Pyro4


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class GumballMachine(GumballMachineRemote):

    SERIALIZER = "json"

    def __init__(self,
                 location: str,
                 number_gumballs: int
                 ) -> None:
        self._sold_out_state = SoldOutState(self)
        self._no_quarter_state = NoQuarterState(self)
        self._has_quarter_state = HasQuarterState(self)
        self._sold_state = SoldState(self)
        self._winner_state = WinnerState(self)
        self._location = location
        self._count = number_gumballs
        self.serializer = Pyro4.util.get_serializer(self.SERIALIZER)
        if number_gumballs > 0:
            self._state = self._no_quarter_state
        else:
            self._state = self._sold_out_state

    def insert_quarter(self) -> None:
        self._state.insert_quarter()

    def eject_quarter(self) -> None:
        self._state.eject_quarter()

    def turn_crank(self) -> None:
        self._state.turn_crank()
        self._state.dispense()

    def set_state(self, state) -> None:
        self._state = state

    def release_ball(self) -> None:
        print("A gumball comes rolling out the slot...")
        if self._count != 0:
            self._count -= 1

    def get_location(self) -> str:
        return self._location

    def get_count(self) -> int:
        return self._count

    def refill(self, count) -> None:
        self._count = count
        self._state = self._no_quarter_state

    def get_state(self) -> State:
        """ serialize state class """
        return pickle.dumps(self._state)

    def get_sold_out_state(self) -> SoldOutState:
        return self._sold_out_state

    def get_no_quarter_state(self) -> NoQuarterState:
        return self._no_quarter_state

    def get_has_quarter_state(self) -> HasQuarterState:
        return self._has_quarter_state

    def get_sold_state(self) -> SoldState:
        return self._sold_state

    def get_winner_state(self) -> WinnerState:
        return self._winner_state

    def __str__(self) -> str:
        result = ""
        result += "\nMighty Gumball, Inc."
        result += "\nJava-enabled Standing Gumball Model #2004"
        result += f"\nInventory: {str(self._count)} gumball"
        if self._count != 1:
            result += "s"
        result += "\n"
        result += f"Machine is {str(self._state)}\n"
        return result
