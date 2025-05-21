


#The super()Funcation
#Assigment :
#Create a class person with a constructer that sets the name.Inherit a class Teacher from it. add a subject field and super()to call the base class constucter.




             # Solution

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with the name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher teaches: {self.subject}")

# Creating an instance of Teacher
t = Teacher("Samina", "GIAIC Python Course")
