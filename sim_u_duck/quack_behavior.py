"""Quack Behavior
"""


from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self) -> None:
        """Quack"""


class Quack(QuackBehavior):
    def quack(self) -> None:
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self) -> None:
        print("<< Silence >>")


class Squeak(QuackBehavior):
    def quack(self) -> None:
        print("Squeak")
