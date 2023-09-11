"""
Plan #1: Create a duck superclass from which all other ducks inherit.
"""

class Duck:
    def quack(self):
        ... # All ducks quack and swim!

    def swim(self):
        ... # All ducks quack and swim!

    def display(self):
        raise NotImplementedError

class MallardDuck(Duck):
    def display(self):
        print("Looks like a Mallard")

class RedheadDuck(Duck):
    def display(self):
        print("Looks like a readhead")

"""
But what happens when we need ducks to fly?
- We need to add a fly() method to ALL the Duck classes
    and then the ducks wlil inherit it.
- But now what happens with RubberDucks, which don't fly?
    * Turns out that not all subclasses of Duck should fly.
    * PROBLEM: Adding something to a superclass that isn't appropriate for all the duck subclasses.
- What turned out great for the purpose of reuse has not turned out great for maintenance.
- What if I override fly() in subclasses to do nothing?
    * Then you have to override every subclass forever! What if you forget?
"""
