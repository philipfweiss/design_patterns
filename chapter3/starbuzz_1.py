from dataclasses import dataclass

"""
What are some problems with this approach? 
- Price changes for condiments requires us to change our code.
- New condiments force us to add new methods to alter the cost of the superclass.
- For new types of beverages, they will inherit the components var.
- What if the customer wants a double mocha?
"""
@dataclass
class BeverageComponent:
    milk: bool = None
    soy: bool = None
    mocha: bool = None
    whip: bool = None
    description: bool = None

class Beverage:
    def __init__(self):
        self.components = BeverageComponent()
    
    def cost(self):
        ...

class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self.components.description = 'dark roast'

class Milk(Beverage):
    def __init__(self):
        super().__init__()
        self.components.milk = 'milk'


print(DarkRoast().components.description)
print(Milk().components.description)
