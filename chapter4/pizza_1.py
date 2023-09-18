class Pizza:
    def prepare(self):
        return self
    
    def bake(self):
        return self

    def cut(self):
        return self

    def box(self):
        return

class CheesePizza(Pizza): ...
class GreekPizza(Pizza): ...
class PepPizza(Pizza): ...


"""
Example of using `if` statements to generate different object types.
Instead, just use a factory!
"""
class PizzaFactory:
    def order_pizza(pizza_type):
        if pizza_type == "cheese":
            pizza = CheesePizza()
        elif pizza_type == "greek":
            pizza = GreekPizza()
        elif pizza_type == "pep":
            pizza = PepPizza()
        else:
            pizza = Pizza()

        return pizza.prepare().bake().cut().box()

"""
The factory isn't really a design pattern, it is more of
a programming idiom. But it is commonly used. 
"""