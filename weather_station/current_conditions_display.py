from display_element import DisplayElement

from observer import Observer

from weather_data import WeatherData


class CurrentConditionsDisplay(DisplayElement, Observer):

    def __init__(self, weather_data: WeatherData) -> None:
        self._temperature = None
        self._humidity = None
        self._weather_data = weather_data

        weather_data.register_observer(self)
    

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        # update state
        self._temperature = temp
        self._humidity = humidity
        _ = pressure

        # update the display
        self.display()
    

    def display(self) -> None:
        print(f"Current conditions: {self._temperature}F degrees and {self._humidity}% humidity")
