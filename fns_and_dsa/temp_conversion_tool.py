FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
     result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
     return result

def convert_to_fahrenheit(celsius):
    result = (celsius * (CELSIUS_TO_FAHRENHEIT_FACTOR)) + 32
    return result

try:
    temperature = float(input("Enter the temperature to convert: "))
except ValueError:
    print("Error! Enter a numerical value.")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if unit == "C":
    converted_temperature = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temperature}F")  
elif unit == "F":
    converted_temperature = convert_to_celsius(temperature)
    print(f"{temperature}F is {converted_temperature}°C")   
else:
    print("Enter correct unit")
    
    
    



