from turkey import WildTurkey, TurkeyAdapter
from duck import MallarDuck, DuckAdapter


def main():
    duck = MallarDuck()
    turkey = WildTurkey()

    turkey_adapter = TurkeyAdapter(turkey)
    duck_adapter = DuckAdapter(duck)
    print(f"The Turkey says..")
    turkey.gobble()
    turkey.fly()

    print(f"\nThe Duck says..")
    duck.quack()
    duck.fly()

    print(f"\nThe TurkeyAdapter says...")
    turkey_adapter.quack()
    turkey_adapter.fly()

    print(f"\nThe DuckAdapter says...")
    duck_adapter.gobble()
    duck_adapter.fly()


if __name__ == "__main__":
    main()
