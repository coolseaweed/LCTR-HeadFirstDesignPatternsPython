from abstract import State
import random


class HasQuarterState(State):
    def __init__(self, gumball_machine) -> None:
        self._gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("You can't insert another quarter")

    def eject_quarter(self) -> None:
        print("Quarter returned")
        self._gumball_machine.set_state(
            self._gumball_machine.get_no_quarter_state())

    def turn_crank(self) -> None:
        print("You turned...")
        winner = random.randint(1, 10)
        if (winner == 1) and (self._gumball_machine.get_count() > 1):
            self._gumball_machine.set_state(
                self._gumball_machine.get_winner_state())
        else:
            self._gumball_machine.set_state(
                self._gumball_machine.get_sold_state())

    def dispense(self) -> None:
        print("No gumball dispensed")

    def __str__(self) -> str:
        return "Waiting for turn of the crank"


class NoQuarterState(State):

    def __init__(self, gumball_machine) -> None:
        self._gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("You inserted a quarter")
        self._gumball_machine.set_state(
            self._gumball_machine.get_has_quarter_state())

    def eject_quarter(self) -> None:
        print("You haven't inserted a quarter")

    def turn_crank(self) -> None:
        print("You turned, but there's no quarter")

    def dispense(self) -> None:
        print("You need to pay first")

    def __str__(self) -> str:
        return "waiting for quarter"


class SoldOutState(State):

    def __init__(self, gumball_machine) -> None:
        self._gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("You can't insert a quarter, the machine is sold out")

    def eject_quarter(self) -> None:
        print("You can't eject, you haven't inserted a quarter yet")

    def turn_crank(self) -> None:
        print("You turned, but there are no gumballs")

    def dispense(self) -> None:
        print("No gumball dispensed")

    def __str__(self) -> str:
        return "sold out"


class SoldState(State):

    def __init__(self, gumball_machine) -> None:
        self._gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("Please wait, we're already giving you a gumball")

    def eject_quarter(self) -> None:
        print("Sorry, you already turned the crank")

    def turn_crank(self) -> None:
        print("Turning twice doesn't get you another gumball!")

    def dispense(self) -> None:
        self._gumball_machine.release_ball()
        if self._gumball_machine.get_count() > 0:
            self._gumball_machine.set_state(
                self._gumball_machine.get_no_quarter_state())
        else:
            print("Oops, out of gumballs!")
            self._gumball_machine.set_state(
                self._gumball_machine.get_sold_out_state())

    def __str__(self) -> str:
        return "dispensing a gumball"


class WinnerState(State):

    def __init__(self, gumballmachine) -> None:
        self._gumballmachine = gumballmachine

    def insert_quarter(self) -> None:
        print("Please wait, we're already giving you a Gumball")

    def eject_quarter(self) -> None:
        print("Please wait, we're already giving you a Gumball")

    def turn_crank(self) -> None:
        print("Turning again doesn't get you another gumball!")

    def dispense(self) -> None:
        self._gumballmachine.release_ball()
        if self._gumballmachine.get_count() == 0:
            self._gumballmachine.set_state(
                self._gumballmachine.get_sold_out_state())
        else:
            print("YOU'RE A WINNER! You get two gumballs for your quarter")

            if self._gumballmachine.get_count() > 0:
                self._gumballmachine.release_ball()
                self._gumballmachine.set_state(
                    self._gumballmachine.get_no_quarter_state())
            else:
                print("Oops, out of gumballs!")
                self._gumballmachine.set_state(
                    self._gumballmachine.get_sold_out_state())

    def __str__(self) -> str:
        return "despensing two gumballs for your quarter, because YOU'RE A WINNER!"
