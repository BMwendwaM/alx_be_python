# Temp conversion F or C
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_fahrenheit(celsius):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR)  + 32
    
    return celsius

def convert_to_celsius(fahrenheit):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return fahrenheit

temperature = float(input("Enter the temperature to convert: "))
format = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if format == "C":
    temperature_new = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {temperature_new}°F")
elif format == "F":
    temperature_new = convert_to_celsius(temperature)
    print(f"{temperature}°F is {temperature_new}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")