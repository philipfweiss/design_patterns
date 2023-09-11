class FlyBehaviour():
    def fly(): ...

class QuackBehaviour():
    def quack(): ... 

class FlyWithWings(FlyBehaviour):
    def fly(): print("wooosh")

class FlyNoWay(FlyBehaviour):
    def fly(): print("crash!")

class Quack(QuackBehaviour):
    def quack(): print("quack!")

class Squeak(QuackBehaviour):
    def quack(): print("squeak!")


class Duck:
    quack_bahaviour = None
    fly_behaviour = None

    def perform_quack(self):
        self.quack_behaviour.quack()
    
    def perform_fly(self):
        self.fly_behaviour.fly()

class MallardDuck(Duck):
    def __init__(self):
        self.quack_behaviour = Squeak()
        self.fly_behaviour = FlyWithWings()
    
    def set_fly_behaviour(self, fly_behaviour):
        self.fly_behaviour = fly_behaviour
    
    def set_quack_behaviour(self, quack_behaviour):
        self.quack_bahaviour = quack_behaviour

