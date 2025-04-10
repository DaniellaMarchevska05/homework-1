import math
import logging
from datetime import datetime

logging.basicConfig(filename='calculator.log', level=logging.INFO)

def square_root(a):
    return math.sqrt(a)


def add(a, b):
    result = a + b
    logging.info(f"{datetime.now()}: ADD - {a} + {b} = {result}")
    return result


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Calculator:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")

    choice = input("Enter operation (1/2/3/4/5): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number (skip if entered '5'): "))

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    elif choice == '5':
        print(f"Result: {square_root(num1)}")
    else:
        print("Invalid input")