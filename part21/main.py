# Make a Custom Class Iterabel:
#Assigment:
#Create a class  Countdown that takes a start number. Implement _ _()and _ _next _ _()to make the object iterable in a for_loop,counting down to 0.


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.count_down = self.start
        return self

    def __next__(self):
        if self.count_down < 0:
            raise StopIteration
        else:
            current = self.count_down
            self.count_down -= 1
            return current

# Testing the Countdown class
for number in Countdown(6):
    print(number)
#6
#5
#4
#3
#2
#1
#0      
        
