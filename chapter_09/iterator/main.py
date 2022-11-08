from menu import *
from waitress import *


def main() -> None:

    # ADD cafe menu
    cafe_menu = CafeMenu()
    cafe_menu.add_item(
        "Veggie Burger and Air Fries",
        "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
        True, 3.99)
    cafe_menu.add_item(
        "Soup of the day",
        "A cup of the soup of the day, with a side salad",
        False, 3.69)
    cafe_menu.add_item(
        "Burrito",
        "A large burrito, with whole pinto beans, salsa, guacamole",
        True, 4.29)

    # ADD dinner menu
    diner_menu = DinerMenu()

    diner_menu.add_item(
        "Vegetarian BLT",
        "(Fakin') Bacon with lettuce & tomato on whole wheat",
        True, 2.99)
    diner_menu.add_item(
        "BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99)
    diner_menu.add_item(
        "Soup of the day",
        "Soup of the day, with a side of potato salad",
        False, 3.29)
    diner_menu.add_item(
        "Hotdog",
        "A hot dog, with sauerkraut, relish, onions, topped with cheese",
        False, 3.05)
    diner_menu.add_item(
        "Steamed Veggies and Brown Rice",
        "A medly of steamed vegetables over brown rice",
        True, 3.99)
    diner_menu.add_item(
        "Pasta",
        "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
        True, 3.89)

    waitress = Waitress(cafe_menu, diner_menu)
    waitress.print_menu()
    print("\nCustomer asks, is the Hotdog vegetarian?")
    print("Waitress says: ", end="")
    if waitress.is_item_vegetarian("Hotdog"):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
