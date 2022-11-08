
import Pyro4
import sys
from gumball_monitor import GumballMonitor
from gumball_machine import GumballMachine
import pickle
import base64


def main():

    sys.excepthook = Pyro4.util.excepthook

    uri_list = [
        f"PYRO:test1.GumballMachine@localhost:9091",
        f"PYRO:test2.GumballMachine@localhost:9092",
        f"PYRO:test3.GumballMachine@localhost:9093",
    ]
    monitor_list = []

    for uri in uri_list:
        try:
            gumball_machine = Pyro4.Proxy(uri)
            monitor = GumballMonitor(gumball_machine)
            gumball_machine.insert_quarter()
            gumball_machine.turn_crank()
            monitor_list.append(monitor)
        except Exception as e:
            print(e)

    for monitor in monitor_list:
        res = monitor.report()
        print(res)


if __name__ == '__main__':

    main()
