import math
# Program to make a simple calculator

# Adds two numbers
def add(x, y):
    return x + y

# Subtracts two numbers
def subtract(x, y):
    return x - y

# Multiplies two numbers
def multiply(x, y):
    return x * y

# Divides two numbers
def divide(x, y):
    return x / y

# Powers a base number (x) by an exponent (y)
def power(x, y):
    return pow(x,y)

# Calculates the square root of a given number (x)
def power(x):
    return math.sqrt(x)

# Calculates the percentage (y) of a given number (x)
def percentage(x,y):
    return y / 100 * x

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Percentage")
print("7.Root")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "^", num2, "=", power(num1, num2))
        elif choice == '6':
            print(num2, "% of", num1, "=", percentage(num1, num2))
    elif choice in ('7'):
        num3 = float(input("Enter first number: "))

        if choice == '7':
            print(num3, "square root =", power(num3)) 
    else:
        print("Invalid Input")

    # check if user wants another calculation
    # break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
    
