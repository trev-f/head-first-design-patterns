"""Mini Duck Simulator
"""


from mallard_duck import MallardDuck


class MiniDuckSimulator:
    def __init__(self) -> None:
        mallard = MallardDuck()
        mallard.perform_quack()
        mallard.perform_fly()


def main():
    MiniDuckSimulator()


if __name__ == "__main__":
    main()
