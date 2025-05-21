#ASsigment:
#Assigment
#Create a class Engine and class Car:Use Composition by passing an Engin object to the Car class during initialization.Access a method of the Engin class via the Car class.




class Engine:
    def start(self):
        print("Engine started!")


class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition (Engine کا object)

    def start_engine(self):
        self.engine.start()  # Accessing Engine's method


# Example usage:
engine = Engine()
car = Car(engine)
car.start_engine()
#output: Engine started
