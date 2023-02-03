from beverage import Beverage


class CondimentDecorator(Beverage):
    """Abstract class that decorates the Beverage class
    """

    _beverage: Beverage = None

    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage
