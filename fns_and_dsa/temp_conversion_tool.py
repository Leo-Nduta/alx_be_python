FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

try:
    temp = float(input("Enter the temperature to convert: "))
    temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").capitalize()
    if temp_unit == "C":
        converted_temp = float((temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32)
        print(f"{temp}°C is {converted_temp}°F")
    else:
            converted_temp = float((temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR)
            print(f"{temp }°F is {converted_temp}°C")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")