from subject import Subject

from observer import Observer


class WeatherData(Subject):
    """A concrete implementation of Subject that represents weather data
    """
    
    def __init__(self) -> None:
        self.observers = []


    # implement the subject interface
    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)
    

    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)
    

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update(temp=self.temperature, humidity=self.humidity, pressure=self.pressure)
    

    # change weather data
    def measurements_changed(self) -> None:
        """Notify observers of changed weather data.
        """
        self.notify_observers()
    

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurements_changed()
