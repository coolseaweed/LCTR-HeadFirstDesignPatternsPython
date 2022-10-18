from abstract import Observer, Subject


class WeatherData(Subject):
    def __init__(self) -> None:
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify_observer(self) -> None:
        """ push info. (subject -> observer) """
        for observer in self.observers:
            observer.update()

    def measurements_changed(self) -> None:
        self.notify_observer()

    def set_measurements(self, temperature, humidity, pressure) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

    def get_temperature(self) -> float:
        return self.temperature

    def get_humidity(self) -> float:
        return self.humidity

    def get_pressure(self) -> float:
        return self.pressure

    def show_obervers(self) -> None:
        print(f"curr observer lists: ")
        [print(f"* {obs}") for obs in self.observers]
        print(f"-----------------------")
