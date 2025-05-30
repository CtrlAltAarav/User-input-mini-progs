import math

def calculator():
    print("------ Advanced Calculator ------")
    print("Available operations:")
    print(" +   → Addition")
    print(" -   → Subtraction")
    print(" *   → Multiplication")
    print(" /   → Division")
    print(" %   → Percentage")
    print(" ^   → Power (x^y)")
    print(" sqrt → Square root")

    while True:
        op = input("\nEnter operation (+, -, *, /, %, ^, sqrt) or 'q' to quit: ")

        if op == 'q':
            print("Calculator closed.")
            break

        if op == "sqrt":
            num = float(input("Enter number: "))
            print("√", num, "=", math.sqrt(num))
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero.")
        elif op == "%":
            print("Result:", (num1 * num2) / 100)
        elif op == "^":
            print("Result:", math.pow(num1, num2))
        else:
            print("Invalid operation!")

calculator()
