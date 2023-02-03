from beverage import Beverage


class HouseBlend(Beverage):
    """Representation of a house blend beverage
    """

    def __init__(self) -> None:
        self.description = 'House Blend Coffee'
    
    def cost(self) -> int:
        return 89
