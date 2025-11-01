# Python Calculator
# Author: Kunal Tibe
# Description: A simple command-line calculator for basic arithmetic operations.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Please enter the operator (+ - * /): ")
result = 0

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")
