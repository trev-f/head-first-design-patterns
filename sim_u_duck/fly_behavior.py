"""Fly Behavior
"""


from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    """An abstract representation of a fly behavior.
    """
    
    @abstractmethod
    def fly(self) -> None:
        """Fly
        """


class FlyWithWings(FlyBehavior):
    """Fly behavior with wings
    """

    def fly(self) -> None:
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):
    """Fly behavior when object shouldn't fly at all.
    """

    def fly(self) -> None:
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    """Fly behavior powered by a rocket
    """
    def fly(self) -> None:
        print("I'm flying with a rocket!")
