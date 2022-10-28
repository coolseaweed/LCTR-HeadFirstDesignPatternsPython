from abc import ABCMeta


class MenuComponent(metaclass=ABCMeta):

    def add(self, menu_component):
        raise NotImplementedError()

    def remove(self, menu_component):
        raise NotImplementedError()

    def get_child(self, i):
        raise NotImplementedError()

    def get_name(self):
        raise NotImplementedError()

    def get_description(self):
        raise NotImplementedError()

    def get_price(self):
        raise NotImplementedError()

    def is_vegetarian(self):
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()
