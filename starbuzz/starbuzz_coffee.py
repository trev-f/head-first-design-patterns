from dark_roast import DarkRoast
from house_blend import HouseBlend
from mocha import Mocha
from espresso import Espresso
from soy import Soy
from whip import Whip


class StarbuzzCoffee:
    """The Starbuzz coffee program
    """

    def main() -> None:
        beverage = Espresso()
        print(f"{beverage.description}: ${beverage.cost()/100}")

        beverage2 = DarkRoast()
        beverage2 = Mocha(beverage2)
        beverage2 = Mocha(beverage2)
        beverage2 = Whip(beverage2)
        print(f"{beverage2.description}: ${beverage2.cost()/100}")

        beverage3 = HouseBlend()
        beverage3 = Soy(beverage3)
        beverage3 = Mocha(beverage3)
        beverage3 = Whip(beverage3)
        print(f"{beverage3.description}: ${beverage3.cost()/100}")


if __name__ == '__main__':
    StarbuzzCoffee.main()
