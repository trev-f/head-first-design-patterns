from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        """Update when weather measurements change

        :param temp: Temperature measured
        :type temp: float
        :param humidity: Humidity measured
        :type humidity: float
        :param pressure: Pressure measured
        :type pressure: float
        """
