#project 6= Build_compose_and_Decorate_A_Complate_Traditional_opp_practies_Series
#Instructor: Samina Saad
#2.Using cls
#Assigment:
# CReate a Class counter that keeps track of how many object have been created. use a class variable and  Class method with cls to manage and display the count.
# soiution   


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_counter(cls):
        print(f"My total created objects are: {cls.count}")

# Objects creation
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()

# Method call
Counter.display_counter()
