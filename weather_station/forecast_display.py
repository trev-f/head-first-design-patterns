from display_element import DisplayElement
from observer import Observer
from weather_data import WeatherData

class ForecastDisplay(DisplayElement, Observer):
    
    def __init__(self, weather_data: WeatherData) -> None:
        self._current_pressure = 29.92
        self._last_pressure = None
        self._weather_data = weather_data

        weather_data.register_observer(self)
    

    def update(self) -> None:
        # pull state
        self._last_pressure = self._current_pressure
        self._current_pressure = self._weather_data.pressure

        # update the display
        self.display()
    

    def display(self) -> None:
        if self._current_pressure == self._last_pressure:
            forecast = 'More of the same'
        elif self._current_pressure > self._last_pressure:
            forecast = 'Improving weather on the way!'
        elif self._current_pressure < self._last_pressure:
            forecast = 'Watch out for cooler, rainy weather.'

        print(f"Forecast: {forecast}")
