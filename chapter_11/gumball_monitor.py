import base64
import pickle


class GumballMonitor():

    def __init__(self, gumball_machine) -> None:
        self._machine = gumball_machine

    def report(self):
        """ methods will be called by network"""

        try:

            state_obj = pickle.loads(base64.b64decode(
                self._machine.get_state()['data']))

            text = ""
            text += f"* machine location: {self._machine.get_location()}\n"
            text += f"* machine ball count: {self._machine.get_count()}\n"
            text += f"* machine state: {state_obj}\n"

            return text
        except Exception as e:
            print(e)
