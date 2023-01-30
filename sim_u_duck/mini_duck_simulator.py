"""Mini Duck Simulator
"""


from mallard_duck import MallardDuck
from model_duck import ModelDuck
from fly_behavior import FlyRocketPowered


class MiniDuckSimulator:
    def __init__(self) -> None:
        mallard = MallardDuck()
        mallard.perform_quack()
        mallard.perform_fly()

        model = ModelDuck()
        model.perform_fly()
        model.fly_behavior = FlyRocketPowered()
        model.perform_fly()


def main():
    MiniDuckSimulator()


if __name__ == "__main__":
    main()
