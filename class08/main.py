import temperature

# Prompt for Celsius input
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = temperature.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit:.2f}°F")

# Prompt for Fahrenheit input
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_converted = temperature.fahrenheit_to_celsius(fahrenheit_input)
print(f"{fahrenheit_input}°F is {celsius_converted:.2f}°C")