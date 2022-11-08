from observer import *
from quack_observable import *
from quackable import *
from abstract_duck_factory import *


class DuckSimulator:

    def simulate_factory(self, duck_factory) -> None:
        print("\nDuck Simulator: With Composite - Flocks")

        flock_of_ducks = Flock()

        flock_of_ducks.add(duck_factory.create_redhead_duck())
        flock_of_ducks.add(duck_factory.create_duck_call())
        flock_of_ducks.add(duck_factory.create_rubber_duck())
        flock_of_ducks.add(GooseAdapter(Goose()))

        flock_of_mallards = Flock()

        for i in range(4):
            flock_of_mallards.add(duck_factory.create_mallard_duck())

        flock_of_ducks.add(flock_of_mallards)

        print("\nDuck Simulator: With Observer")

        quackologist = Quackologist()
        flock_of_ducks.register_observer(quackologist)

        self.simulate_duck(flock_of_ducks)

        print(f"The ducks quacked {str(QuackCounter.get_quacks())} times")

    def simulate_duck(self, duck) -> None:
        duck.quack()


def main() -> None:
    simulator = DuckSimulator()
    duck_factory = CountingDuckFactory()
    simulator.simulate_factory(duck_factory)


if __name__ == "__main__":
    main()
