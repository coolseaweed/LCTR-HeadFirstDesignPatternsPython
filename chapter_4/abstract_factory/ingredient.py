from abstract import *

""" concrete class """


# Cheese
class MozzarellaCheese(Cheese):
    def __str__(self) -> str:
        return "Shredded Mozzarella"


class ParmesanCheese(Cheese):
    def __str__(self) -> str:
        return "Shredded Parmesan"


class ReggianoCheese(Cheese):
    def __str__(self) -> str:
        return "Reggiano Cheese"


# Clams
class FreshClams(Clams):
    def __str__(self) -> str:
        return "Fresh Clams from Long Island Sound"


class FrozenClams(Clams):
    def __str__(self) -> str:
        return "Frozen Clams from Chesapeake Bay"


# Dough
class ThickCrustDough(Dough):
    def __str__(self) -> str:
        return "Thick crust dough"


class ThinCrustDough(Dough):
    def __str__(self) -> str:
        return "Thin Crust Dough"


# Pepperoni
class SlicedPepperoni(Pepperoni):
    def __str__(self) -> str:
        return "Sliced Pepperoni"


# Sauce
class MarinaraSauce(Sauce):
    def __str__(self) -> str:
        return "Marinara Sauce"


class PlumTomatoSauce(Sauce):
    def __str__(self) -> str:
        return "Tomato sauce with plum tomatoes"


# Veggie
class BlackOlives(Veggie):
    def __str__(self) -> str:
        return "Black Olives"


class Eggplant(Veggie):
    def __str__(self) -> str:
        return "Eggplant"


class Garlic(Veggie):
    def __str__(self) -> str:
        return "Garlic"


class Mushroom(Veggie):
    def __str__(self) -> str:
        return "Mushrooms"


class Onion(Veggie):
    def __str__(self) -> str:
        return "Onion"


class RedPepper(Veggie):
    def __str__(self) -> str:
        return "Red Pepper"


class Spinach(Veggie):
    def __str__(self) -> str:
        return "Spinach"
