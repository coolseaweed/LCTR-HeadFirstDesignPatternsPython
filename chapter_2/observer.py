from abstract import Observer, DisplayElement
from subject import WeatherData


# Concrete class
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
