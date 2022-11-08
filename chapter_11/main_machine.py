
import Pyro4
import sys
from gumball_machine import GumballMachine


def main(argv: list):
    '''
    daemon = Pyro4.Daemon('localhost')
    ns = Pyro4.locateNS()
    uri = daemon.register(state_module.GumballMachine)
    ns.register("GumballMachine", uri)
    daemon.requestLoop()
    '''
    location = argv[1]
    num_gumballs = int(argv[2])
    host = argv[3]
    port = int(argv[4])
    print(f"Server waitinig client request..")

    Pyro4.Daemon.serveSimple({
        GumballMachine(location, num_gumballs): f"{location}.GumballMachine"},
        host=host,
        port=port,
        ns=False,
        verbose=True
    )


if __name__ == '__main__':
    print(len(sys.argv))

    if len(sys.argv) < 2:
        print()
        sys.exit(1)

    print(sys.argv[3])
    main(sys.argv)

    # machine_monitor_list = []

    # gumballmachine = GumballMachine(10)
    # print(gumballmachine)

    # for i in range(10):

    #     print(f"iterate: {i+1}")

    #     gumballmachine.insert_quarter()
    #     gumballmachine.turn_crank()
    #     print(gumballmachine)
    #     print("--------------------------\n")
