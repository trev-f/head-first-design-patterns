from beverage import Beverage
from condiment_decorator import CondimentDecorator


class Soy(CondimentDecorator):
    """Representation of a soy condiment
    """

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    @property
    def description(self) -> str:
        return f"{self.beverage.description}, Soy"

    def cost(self) -> int:
        return _15 + self.beverage.cost()
