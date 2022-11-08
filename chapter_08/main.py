
from caffein_beverage import Tea, Coffee, TeaWithHook, CoffeeWithHook

if __name__ == "__main__":
    tea = Tea()
    coffee = Coffee()

    print("\nMaking tea...")
    tea.prepare_recipe()

    print("\nMaking coffee...")
    coffee.prepare_recipe()

    tea_with_hook = TeaWithHook()
    coffee_with_hook = CoffeeWithHook()

    print("\nMaking tea...")
    tea_with_hook.prepare_recipe()

    print("\nMaking coffee...")
    coffee_with_hook.prepare_recipe()
