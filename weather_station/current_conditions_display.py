from display_element import DisplayElement

from observer import Observer

from weather_data import WeatherData


class CurrentConditionsDisplay(DisplayElement, Observer):
    def __init__(self, weather_data: WeatherData) -> None:
        self._temperature = None
        self._humidity = None
        self._weather_data = weather_data

        weather_data.register_observer(self)

    def update(self) -> None:
        # update state
        self._temperature = self._weather_data.temperature
        self._humidity = self._weather_data.humidity

        # update the display
        self.display()

    def display(self) -> None:
        print(
            f"Current conditions: {self._temperature}F degrees and {self._humidity}% humidity"
        )
