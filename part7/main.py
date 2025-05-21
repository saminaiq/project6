




#public(name, department):Aam tor par har jaga accessible.
#protected(-Salary):Subclass access kar sakta hai, lekin directly bhar karna recommended
#private(_ssn):Sirf class ka andaer ya getter method sa access ho sakta hai
#Getter:get_ssn()private data ko safely read karta hai.
#Setter:set_salary()Protected variabel ko valiidate karta set karata hai


















class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary  # protected
        self.__ssn = ssn       # private

    def get_ssn(self):
        return self.__ssn

    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Salary must be a positive number.")

    def display(self):
        print(f"Name: {self.name}")            # public
        print(f"Salary: {self._salary}")       # protected
        print(f"SSN: {self.__ssn}")            # private


class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")
        print(f"Accessing SSN via getter: {self.get_ssn()}")


# object creation and testing
m = Manager("Ali", 1200000, "444-852-2025", "Information Technology")
m.show_manager_info()

# update salary
m.set_salary(32000)
print("Updated Salary:", m._salary)

# accessing private variable via getter
print("Private SSN via getter:", m.get_ssn())
