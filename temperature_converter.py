# Temperature Converter: Celsius <-> Fahrenheit

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("Temperature Converter")
choice = input("Convert from (C)elsius or (F)ahrenheit? ").strip().upper()

if choice == 'C':
    c = float(input("Enter temperature in Celsius: "))
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C is {f:.2f}°F")
elif choice == 'F':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = fahrenheit_to_celsius(f)
    print(f"{f}°F is {c:.2f}°C")
else:
    print("Invalid choice. Please enter 'C' or 'F'.")
