"""Duck

This module implements the Duck superclass as an interface to make other ducks.

Classes:

    * Duck
"""


from abc import ABC, abstractmethod

from fly_behavior import FlyBehavior
from quack_behavior import QuackBehavior


class Duck(ABC):
    """An abstract representation of a duck"""

    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior) -> None:
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    
    @abstractmethod
    def display(self) -> None:
        """Display the duck"""

    def perform_fly(self) -> None:
        """Perform the fly method from the fly behavior.
        """
        self.fly_behavior.fly()
    

    def perform_quack(self) -> None:
        """Perform the quack method from the quack behavior.
        """
        self.quack_behavior.quack()

    
    def swim(self) -> None:
        """Perform the swim behavior.
        """
        print("All ducks float, even decoys!")
