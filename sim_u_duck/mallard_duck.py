"""Mallard Duck
"""


from duck import Duck
from fly_behavior import FlyWithWings
from quack_behavior import Quack


class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self) -> None:
        print("I'm a real mallard duck")
