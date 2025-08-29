# Simple Calculator

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Undefined (division by zero)"

print("Simple Calculator")
print("Select operation: +, -, *, /")
op = input("Enter operator: ")

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if op == '+':
    print("Result:", add(x, y))
elif op == '-':
    print("Result:", subtract(x, y))
elif op == '*':
    print("Result:", multiply(x, y))
elif op == '/':
    print("Result:", divide(x, y))
else:
    print("Invalid operator")
