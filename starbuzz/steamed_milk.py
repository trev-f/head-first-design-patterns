from beverage import Beverage
from condiment_decorator import CondimentDecorator


class SteamedMilk(CondimentDecorator):
    """Representation of a steamed milk condiment
    """

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    @property
    def description(self) -> str:
        return f"{self.beverage.description}, Steamed Milk"

    def cost(self) -> int:
        return _10 + self.beverage.cost()
