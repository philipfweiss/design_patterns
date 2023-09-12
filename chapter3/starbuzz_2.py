class Beverage:
    def __init__(self, description="Unknown Beverage"):
        self.description = description

    def cost(self):
        ...
    
    def get_description(self):
        return self.description

class HouseBlend(Beverage):
    def __init__(self):
        super().__init__(description="House Blend")

    def cost(self):
        return .89

class Espresso(Beverage):
    def __init__(self):
        super().__init__(description="Espresso")

    def cost(self):
        return 1.99

class CondimentDecorator(Beverage):
    def __init__(self):
        self.beverage = Beverage()
    
    def get_description(self):
        return self.beverage.get_description()

class Milk(CondimentDecorator):
    def cost(self):
        ...

    def get_description(self):
        return super().get_description()


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + .20

    def get_description(self):
        return super().get_description() + "+Mocha"

class Soy(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + .20

    def get_description(self):
        return super().get_description() + "+Soy"


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + .1

    def get_description(self):
        return super().get_description() + "+Whip"

beverage = Mocha(Soy(Whip(Whip(Espresso()))))
print(beverage.get_description())
print(beverage.cost())