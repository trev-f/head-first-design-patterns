from beverage import Beverage


class Espresso(Beverage):
    """Representation of an espresso beverage
    """

    def __init__(self) -> None:
        self.description = 'Espresso'

    def cost(self) -> int:
        return 1_99
