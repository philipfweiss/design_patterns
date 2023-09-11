class Measurement:
    temp: int
    pressure: int
    humidity: int

class Subject:
    observers = set()

    def register(self, observer):
        self.observers.add(observer)

    def remove(self, observer):
        self.observers.remove(observer)

    def notify(self): ...

class Display: ...

class Observer:
    def update(self, measurement): ...

class WeatherData(Subject):
    measurement: Measurement

    def notify(self):
        for observer in self.observers:
            observer.update(self.measurement)
    
    def get_temp(self):
        ...
    
    def get_humidity(self):
        ...
    
    def get_pressure(self):
        ...
    
    def measurements_changed(self):
        self.measurement = Measurement(
            temp=self.get_temp(),
            humidity=self.get_humidity(),
            pressure=self.get_pressure(),
        )
        self.notify()

class ADisplay(Observer, Display): ...
class BDisplay(Observer, Display): ...
class CDisplay(Observer, Display): ...
