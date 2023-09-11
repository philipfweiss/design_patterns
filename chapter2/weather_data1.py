"""
This implementation is problematic because:
- We are coding to concrete implementations.
- Cannot change display without changing code.
- We cannot remove or add displays at runtime
- WeatherData class is not encapsulated
"""

def get_temp(): ...
def get_pressure(): ...
def get_humidity(): ...

class CurrentConditionsDisplay:
    temp: int
    pressure: int
    humidity: int

    def update(self, temp, pressure, humidity):
        self.temp = temp
        self.pressure = pressure
        self.humidity = humidity

class WeatherData:
    def __init__(self):
        self.display = CurrentConditionsDisplay()

    def measurements_changed(self):
        temp, pressure, humidity = get_temp(), get_pressure(), get_humidity()
        self.display.update(temp, pressure, humidity)
        # self.statistics_display.update(...) 
        # self.forecast_display.update(...)

