#project 6:Build_compose_and_Decorter_A-complete_oop_parictice_SEries
#Instucter:Samina

#9.Abstract Classes and Methods
#Assigment:
#Use the abc mpodule to create an abstract class shape with an abstract method area(). Inherit a class Rectangle that implements


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create object
rect = Rectangle(5, 8)
print("Area of Rectangle:", rect.area())
