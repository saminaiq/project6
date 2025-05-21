#Class Decorators :
#Assigment:
#Create a class decocrator add_greeting that modifies a class to add a greet () method returing "Hello from Decorator!".Apply it to a class person


# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Adding greet method to the class
    return cls

# Applying decorator to class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Creating object and testing
p = Person("Ali")
print(p.greet())  # Output: Hello from Decorator!
#output
#Hello from Decorator!
