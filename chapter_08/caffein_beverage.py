from abstract import CaffeinBeverage, CaffeineBeverageWithHook


class Tea(CaffeinBeverage):

    def brew(self) -> None:
        print(f"Steeping the tea")

    def add_condiments(self) -> None:
        print(f"Adding Lemon")


class Coffee(CaffeinBeverage):

    def brew(self) -> None:
        print("Dripping Coffee through filter")

    def add_condiments(self) -> None:
        print("Adding Sugar and Milk")


class CoffeeWithHook(CaffeineBeverageWithHook):

    def brew(self) -> None:
        print("Dripping Coffee through filter")

    def add_condiments(self) -> None:
        print("Adding Sugar and Milk")

    def customer_wants_condiments(self):
        prompt = "Would you like milk and sugar with your coffee (y/n)? "
        answer = input(prompt)
        return answer.lower().startswith('y')


class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self) -> None:
        print("Stepping the tea")

    def add_condiments(self) -> None:
        print("Adding Lemon")

    def customer_wants_condiments(self):
        prompt = "Would you like lemmon with your tea (y/n)? "
        answer = input(prompt)
        return answer.lower().startswith('y')
