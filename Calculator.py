# Simple Calculator Application

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Welcome to the Calculator Application")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("Enter 'q' to quit")

    while True:
        # Get operation choice from the user
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting Calculator. Goodbye!")
            break

        # Check if the choice is a valid operation (ensure choice is a string)
        if choice in ['1', '2', '3', '4']:  
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")

                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")

                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")

                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")

            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid operation.")

# Run the calculator
calculator()
