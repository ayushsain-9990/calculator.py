
# Simple Calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


print("===== SIMPLE CALCULATOR =====")

# Taking two inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    result = add(num1, num2)
    print("Result:", result)

elif choice == "2":
    result = subtract(num1, num2)
    print("Result:", result)

elif choice == "3":
    result = multiply(num1, num2)
    print("Result:", result)

elif choice == "4":
    result = divide(num1, num2)
    print("Result:", result)

else:
    print("Invalid choice! Please select between 1 and 4.")