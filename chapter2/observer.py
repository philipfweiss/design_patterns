class Subject:
    def register(self, observer): ...
    def remove(self, observer): ...
    def notify(self): ...

class Observer:
    def update(self, update): ...

class ConcreteSubject(Subject):
    observers = set()
    def register(self, observer):
        self.subjects.add(observer)
    
    def remove(self, observer):
        self.subjects.remove(observer)
    
    def notify(self, update):
        for observer in self.observers:
            observer.update(update)
