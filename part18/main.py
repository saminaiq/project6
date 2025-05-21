#porperty Decorators:@property,@setter,and @deleter
#Assigment:
#Create a class product with a private attribut_price.Use @property to get the price. @price.setter to update it, and @price.deleter to delet it.




class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    # Getter
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    # Deleter
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Testing the class
p = Product(100)

# Get price
print(p.price)  # Output: 100

# Set price
p.price = 150
print(p.price)  # Output: 150

# Delete price
del p.price
