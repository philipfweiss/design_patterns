# Programming to an implementation:
class Animal: 
    def makesound(self): ...

class Dog(Animal):
    def bark(self):
        print("woof!")

def get_animal(): ...

# Declaring dog forces us to code to a concrete implementation
dog = Dog()
dog.bark()

# We know it's a dog, but we can use the animal reference polymorphically.
animal = Dog()
animal.makesound()

# Even better, do the following (we don't know what the animal subtype is!)
a = get_animal()
a.makesound()
