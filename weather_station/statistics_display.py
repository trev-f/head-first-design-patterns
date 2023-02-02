import statistics

from display_element import DisplayElement
from observer import Observer
from weather_data import WeatherData


class StatisticsDisplay(DisplayElement, Observer):
    def __init__(self, weather_data: WeatherData) -> None:
        self._temperatures = []
        self._weather_data = weather_data

        weather_data.register_observer(self)

    def update(self) -> None:
        # pull state
        self._temperatures.append(self._weather_data.temperature)

        # update the display
        self.display()

    def display(self) -> None:
        temp_mean = statistics.fmean(self._temperatures)
        temp_max = max(self._temperatures)
        temp_min = min(self._temperatures)

        print(f"Avg/Min/Max temperature = {temp_mean}/{temp_max}/{temp_min}")
