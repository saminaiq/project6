#Aggregation
#ASsigment
#Create a class Department and a class Employee. use aggregation by having a Department object store a refernce to an Emplpoyee object that exists independently of it.





class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")


class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: reference to an existing Employee

    def show_department_details(self):
        print(f"Department: {self.department_name}")
        self.employee.display()


# Independent Employee object
emp1 = Employee("Ali", 101)

# Department object that aggregates the Employee
dept1 = Department("HR", emp1)

# Display information
dept1.show_department_details()
#output: Department Name : HR, Employee Name:Samina saad



