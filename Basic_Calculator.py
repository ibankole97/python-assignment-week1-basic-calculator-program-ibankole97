print("BASIC CALCULATOR")

# Accept two numbers and an operation from the user
num1 = float(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the calculation based on the operation
if operation == "+":
    print(f"The result is: {num1 + num2}")
elif operation == "-":
    print(f"The result is: {num1 - num2}")
elif operation == "*":
    print(f"The result is: {num1 * num2}")
elif operation == "/":
    if num2 != 0:  # Check for division by zero
        print(f"The result is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
    