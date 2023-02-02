"""Model Duck
"""


from duck import Duck
from fly_behavior import FlyNoWay
from quack_behavior import Quack


class ModelDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self) -> None:
        print("I'm a model duck")
