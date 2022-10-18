from pizza_store import NYPizzaStore, ChicagoPizzaStore

""" Abstract Factory Pattern """


def main() -> None:
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.order_pizza("cheese")
    print(f"Ethan ordered a [{pizza.get_name()}]\n{str(pizza)}\n")

    pizza = chicagoStore.order_pizza("cheese")
    print(f"Joel ordered a [{pizza.get_name()}]\n{str(pizza)}\n")

    pizza = nyStore.order_pizza("clam")
    print(f"Ethan ordered a [{pizza.get_name()}]\n{str(pizza)}\n")

    pizza = chicagoStore.order_pizza("clam")
    print(f"Joel ordered a [{pizza.get_name()}]\n{str(pizza)}\n")

    pizza = nyStore.order_pizza("pepperoni")
    print(f"Joel ordered a [{pizza.get_name()}]\n{str(pizza)}\n")

    pizza = chicagoStore.order_pizza("pepperoni")
    print(f"Ethan ordered a [{pizza.get_name()}]\n{str(pizza)}\n")

    pizza = nyStore.order_pizza("veggie")
    print(f"Joel ordered a [{pizza.get_name()}]\n{str(pizza)}\n")


if __name__ == "__main__":
    main()
