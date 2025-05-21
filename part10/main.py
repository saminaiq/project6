#project 6:
#Instroucter:Samina

#10.Instance Mrthods
#Assigment:
# CReate a Class Dog withe instance variable .add an instance method bark()that prints a message including the dogs,s name,




class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: woof woof!")

# Create object and call method
dog1 = Dog("Buddy", "Aidi")
dog1.bark()
