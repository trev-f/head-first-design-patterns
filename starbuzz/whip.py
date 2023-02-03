from beverage import Beverage
from condiment_decorator import CondimentDecorator


class Whip(CondimentDecorator):
    """Representation of a whip condiment
    """

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    @property
    def description(self) -> str:
        return f"{self.beverage.description}, Whip"

    def cost(self) -> int:
        return _10 + self.beverage.cost()
