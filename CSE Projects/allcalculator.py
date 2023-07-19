import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed."

def calculate_tax(amount, tax_rate):
    return amount * tax_rate / 100

def main():
    print("Welcome to AllCalculator!")
    
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    print("The sum is: ", add(first_number, second_number))
    print("The difference is: ", subtract(first_number, second_number))
    print("The product is: ", multiply(first_number, second_number))
    print("The quotient is: ", divide(first_number, second_number))
    
    amount = float(input("Enter the amount for tax calculation: "))
    tax_rate = float(input("Enter the tax rate (in percentage): "))
    print("The calculated tax is: ", calculate_tax(amount, tax_rate))

if __name__ == "__main__":
    main()
