from abstract import Pizza


# NYStyle Pizza
class NYStyleCheesePizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "NY Style Sauce and Cheese Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")


class NYStylePepperoniPizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "NY Style Pepperoni Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")
        self._toppings.append("Sliced Pepperoni")
        self._toppings.append("Garlic")
        self._toppings.append("Onion")
        self._toppings.append("Mushrooms")
        self._toppings.append("Red Pepper")


class NYStyleClamPizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "NY Style Clam Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")
        self._toppings.append("Fresh Clams from Long Island Sound")


class NYStyleVeggiePizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "NY Style Veggie Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")
        self._toppings.append("Garlic")
        self._toppings.append("Onion")
        self._toppings.append("Mushrooms")
        self._toppings.append("Red Pepper")


# ChicagoStyle Pizza
class ChicagoStyleCheesePizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "Chicago Style Deep Dish Cheese Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"
        self._toppings.append("Shredded Mozzarella Cheese")

    def cut(self) -> None:
        print("- Cutting the pizza into square slices")


class ChicagoStylePepperoniPizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "Chicago Style Pepperoni Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"

        self._toppings.append("Shredded Mozzarella Cheese")
        self._toppings.append("Black Olives")
        self._toppings.append("Spinach")
        self._toppings.append("Eggplant")
        self._toppings.append("Sliced Pepperoni")

    def cut(self) -> None:
        print("- Cutting the pizza into square slices")


class ChicagoStyleClamPizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "Chicago Style Clam Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"

        self._toppings.append("Shredded Mozzarella Cheese")
        self._toppings.append("Frozen Clams from Chesapeake Bay")

    def cut(self) -> None:
        print("- Cutting the pizza into square slices")


class ChicagoStyleVeggiePizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self._name = "Chicago Deep Dish Veggie Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"

        self._toppings.append("Shredded Mozzarella Cheese")
        self._toppings.append("Black Olives")
        self._toppings.append("Spinach")
        self._toppings.append("Eggplant")

    def cut(self) -> None:
        print("- Cutting the pizza into square slices")
