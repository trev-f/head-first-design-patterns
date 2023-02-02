from abc import ABC, abstractmethod


class Beverage(ABC):
    """Abstract representation of a beverage
    """

    def __init__(self) -> None:
        self.description = 'Unknown Beverage'

    @abstractmethod
    def cost(self) -> float:
        """Calculate cost
        """
