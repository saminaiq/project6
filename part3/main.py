# project 6 Build_compose_and_Decorate_A_complete _ Traditional _ opp_Practice_Series
# Instructur : Samina 

#3 . public Variables and Methods 
# Assigment :
#Create a class witha a public variabls brand and a public method star (). Instantiate the class  andaccess both from outside the class.
#solution



class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...!")

# object creation and method calls
my_car = Car("Audi")
print(my_car.brand)
my_car.start()

