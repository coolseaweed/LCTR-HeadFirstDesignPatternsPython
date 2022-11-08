
from subject import WeatherData
from observer import CurrentConditionsDisplay, StatisticsDisplay, ForecastDisplay, HeatindexDisplay


def main() -> None:
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


if __name__ == "__main__":
    main()
