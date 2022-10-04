from abc import ABCMeta, abstractmethod


# -------------------------------------
# Abstract classes
# -------------------------------------
class Observer(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def update(self) -> None:
        raise NotImplementedError


class DisplayElement(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError


class Subject(metaclass=ABCMeta):
    """ interface class """

    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def notify_observer(self) -> None:
        raise NotImplementedError


# -------------------------------------
# Implement classes
# -------------------------------------

# subject
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


# observer
class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.temperature = None
        self.humidity = None

    def update(self) -> None:
        self.temperature = self.weather_data.get_temperature()
        self.humidity = self.weather_data.get_humidity()
        self.display()

    def display(self) -> None:
        print(
            f"Current conditions: {self.temperature} F degree and {self.humidity} % humidity")


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data) -> None:
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.max_temp = 0
        self.min_temp = 200
        self.temp_sum = 0
        self.num_readings = 0

    def update(self) -> None:
        temp = self.weather_data.get_temperature()
        self.temp_sum += temp
        self.num_readings += 1
        self.max_temp = max(temp, self.max_temp)
        self.min_temp = min(temp, self.min_temp)
        self.display()

    def display(self) -> None:
        print(
            f"Avg / Max / Min temperature = {(self.temp_sum / self.num_readings):.1f} / {self.max_temp} / {self.min_temp} F")


class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.last_pressure = 0
        self.current_pressure = 0

    def update(self) -> None:
        pressure = self.weather_data.get_pressure()
        self.last_pressure = self.current_pressure
        self.current_pressure = pressure
        self.display()

    def display(self) -> None:

        text = "Forecast: "
        if self.current_pressure > self.last_pressure:
            text += "Improving weather on the way!"
        elif self.current_pressure == self.last_pressure:
            text += "More of the same"
        elif self.current_pressure < self.last_pressure:
            text += "Watch out for cooler, rainy weather"

        print(text)


class HeatindexDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.temperature = 0
        self.humidity = 0

    def update(self) -> None:
        self.temperature = self.weather_data.get_temperature()
        self.humidity = self.weather_data.get_humidity()
        self.display()

    def compute_heatindex(self, t, rh) -> float:
        index = ((16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) +
                  (0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) +
                  (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) +
                  (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 *
                                                                                      (rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) +
                  (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) +
                  0.000000000843296 * (t * t * rh * rh * rh)) -
                 (0.0000000000481975 * (t * t * t * rh * rh * rh)))

        return index

    def display(self) -> None:

        heatindex = self.compute_heatindex(self.temperature, self.humidity)
        print(f"Heat index: {heatindex:.4f} F")


# main
if __name__ == "__main__":
    weather_data = WeatherData()
    ccd = CurrentConditionsDisplay(weather_data)
    sd = StatisticsDisplay(weather_data)
    fd = ForecastDisplay(weather_data)
    hd = HeatindexDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)

    weather_data.show_obervers()
    weather_data.remove_observer(ccd)

    weather_data.show_obervers()
