def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero!"

while True:
    print("\nChoose operation: +, -, *, / or type 'exit' to quit")
    op = input("Operator: ")
    if op == 'exit':
        print("Calculator exited.")
        break
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    if op == '+':
        result = add(num1, num2)
    elif op == '-':
        result = subtract(num1, num2)
    elif op == '*':
        result = multiply(num1, num2)
    elif op == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operator! Please choose +, -, *, or /.")
        continue

    print(f"Result: {num1} {op} {num2} = {result}")
