import math
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='calculator.log', level=logging.INFO)

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

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

    choice = input("Enter operation (1/2/3/4): ")
    num1 = get_number_input("Enter first number: ")
    num2 = get_number_input("Enter second number (skip if entered option '5'): ")

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