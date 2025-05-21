#Ccreating a Custom Exception:
#Assigment:
#Create a custom exception InvalidAgeError.write a funcation check_age(age)that raises this exception if age<18.Handleitwith try...except.



# Custom exception
class InvalidAgeError(Exception):
    """
    Custom exception for Invalid age.
    """
    pass

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Access granted!")

# Testing with try...except
try:
    check_age(16)
except InvalidAgeError as e:
    print(f"Error: {e}")

#Error: Age must be at least 18.



