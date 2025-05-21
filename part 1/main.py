class Student:
    def __init__(self, name, marks):
        self.name = name        # self object attribute 
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Student Marks:", self.marks)

# object 
student1 = Student("Ali", 85)

# method call 
student1.display()
