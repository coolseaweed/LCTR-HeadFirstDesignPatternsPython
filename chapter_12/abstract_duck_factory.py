from abstract import AbstractDuckFactory
from quackable import *


class DuckFactory(AbstractDuckFactory):

    def create_mallard_duck(self) -> MallardDuck:
        return MallardDuck()

    def create_redhead_duck(self) -> RedheadDuck:
        return RedheadDuck()

    def create_duck_call(self) -> DuckCall:
        return DuckCall()

    def create_rubber_duck(self) -> RubberDuck:
        return RubberDuck()


class CountingDuckFactory(AbstractDuckFactory):

    def create_mallard_duck(self) -> QuackCounter:
        return QuackCounter(MallardDuck())

    def create_redhead_duck(self) -> QuackCounter:
        return QuackCounter(RedheadDuck())

    def create_duck_call(self) -> QuackCounter:
        return QuackCounter(DuckCall())

    def create_rubber_duck(self) -> QuackCounter:
        return QuackCounter(RubberDuck())
