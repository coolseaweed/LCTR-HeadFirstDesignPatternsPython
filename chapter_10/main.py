from gumball_machine import GumballMachine


if __name__ == '__main__':
    gumballmachine = GumballMachine(10)
    print(gumballmachine)

    for i in range(10):

        print(f"iterate: {i+1}")

        gumballmachine.insert_quarter()
        gumballmachine.turn_crank()
        print(gumballmachine)
        print("--------------------------\n")
