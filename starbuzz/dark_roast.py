from beverage import Beverage


class DarkRoast(Beverage):
    """Representation of a dark roast beverage
    """

    def __init__(self) -> None:
        self.description = 'Dark Roast Coffee'

    def cost(self) -> int:
        return _99
