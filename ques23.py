
conversion_type = input("Enter 'C to F' to convert Celsius to Fahrenheit or 'F to C' to convert Fahrenheit to Celsius: ")
temperature = float(input("Enter the temperature to convert: "))

if conversion_type == 'C to F':
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted_temperature}°F")
elif conversion_type == 'F to C':
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted_temperature}°C")
else:
    print("Invalid conversion type. Please enter 'C to F' or 'F to C'.")
