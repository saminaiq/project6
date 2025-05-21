# Static Methods 
#Assigment:
# Create a class Temperatuer with a static method celsious_to_fahrenheit(c) that returns the Faherenheit value.



class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        """
        Convert Celsious to Faherenheit

        
        """
        return (c * 9/5) + 32

# Example usage:
temp_1 = TemperatureConverter
print(f"Temperature in Fahrenheit: {temp_1.celsius_to_fahrenheit(25)}°F")

# out put
#Temperature in Fahrenheit: 77.0°F


    