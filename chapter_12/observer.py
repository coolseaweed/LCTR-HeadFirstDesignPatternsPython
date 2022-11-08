from abstract import *


class Quackologist(Observer):

    def update(self, duck) -> None:
        print(f"Quackologist: {str(duck)} just quacked.")

    def __str__(self):
        return "Quackologist"
