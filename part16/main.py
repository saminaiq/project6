#Funcation Decoraters
#Assigment:
#write a decorator funcation log_funcation_cal 1 taht prints"Funcation is being called" befor a funcation executes . Apply it to a funcation say_hello().



# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Applying decorator to a function
@log_function_call
def say_hello():
    print("Hello!")

# Calling the function
say_hello()
#Function is being called
# Hello,
