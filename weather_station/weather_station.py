from current_conditions_display import CurrentConditionsDisplay
from forecast_display import ForecastDisplay
from statistics_display import StatisticsDisplay
from weather_data import WeatherData


class WeatherStation:

    @staticmethod
    def main() -> None:
        weather_data = WeatherData()

        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)

        weather_data.set_measurements(temperature=80, humidity=65, pressure=30.4)
        weather_data.set_measurements(temperature=82, humidity=70, pressure=29.2)
        weather_data.set_measurements(temperature=78, humidity=90, pressure=29.2)


if __name__ == '__main__':
    WeatherStation.main()
