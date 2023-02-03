from beverage import Beverage
from condiment_decorator import CondimentDecorator


class Mocha(CondimentDecorator):
    """Representation of a mocha condiment
    """

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    @property
    def description(self) -> str:
        return f"{self.beverage.description}, Mocha"

    def cost(self) -> int:
        return _20 + self.beverage.cost()
