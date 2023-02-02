from beverage import Beverage


class Decaf(Beverage):
    """Representation of a decaf coffee beverage
    """

    def __init__(self) -> None:
        self.description = 'Decaf coffee'

    def cost(self) -> int:
        return 1_05
