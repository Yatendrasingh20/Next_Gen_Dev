a=float(input("Enter your first number"))
b=float(input("Enter your second number"))

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b    

def calculate(a, b, operator):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return subtract(a, b)
    elif operator == '*':
        return multiply(a, b)
    elif operator == '/':
        return divide(a, b)
    else:
        return "Error: Invalid operator"

operator = input("Enter an operator (+, -, *, /): ")

result = calculate(a, b, operator)

print(f"Result: {result}")