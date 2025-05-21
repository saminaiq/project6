#callable()and _ _call_ _():
#Assigment:
#Create a class  Multiplier with an _ _ init() to set a factor a _ _call_ _()method that multiplies an input by the factor. Test it with callabel()and by calling the object like a funcation.




class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create object
double = Multiplier(2)

# Test with callable()
print(callable(double))  # Output: True

# Call like a function
result = double(5)
print(result)  # Output: 10

#True
10
