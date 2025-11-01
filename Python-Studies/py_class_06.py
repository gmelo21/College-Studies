import time

# Function to ask the user for two numbers, ensuring they are integers
def ask_for_numbers():
    global a
    global b
    while True:
        try:
            a = int(input("First number: "))
            break  # Exit loop if input is valid
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            b = int(input("Second number: "))
            break  # Exit loop if input is valid
        except ValueError:
            print("Please enter a valid number.")


# Function to sum two numbers
def sum(a, b):
    return a + b


# Function to subtract the second number from the first
def subtract(a, b):
    return a - b


# Function to divide the first number by the second Handles division by zero
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed!"

# Function to multiply two numbers
def multiply(a, b):
    return a * b


# Main loop that displays the calculator menu and allows the user to select an operation
while True:
    try:
        # Display operation options
        print()
        print("1 - Sum")
        print("2 - Subtract")
        print("3 - Divide")
        print("4 - Multiply")
        print("0 - End")
        operation = int(input("\nChoose your operation: "))
    except ValueError:
        # If the input is not a valid number, display an error message
        print("Please enter a valid number.")
    else:
        # Perform the operation based on user input
        match operation:
            case 1:
                ask_for_numbers()  # Prompt the user for numbers
                print(sum(a, b))  # Display the result of the sum
            case 2:
                ask_for_numbers()  # Prompt the user for numbers
                print(subtract(a, b))  # Display the result of the subtraction
            case 3:
                ask_for_numbers()  # Prompt the user for numbers
                print(divide(a, b))  # Display the result of the division
            case 4:
                ask_for_numbers()  # Prompt the user for numbers
                # Display the result of the multiplication
                print(multiply(a, b))
            case 0:
                break  # Exit the loop if the user chooses to end the program
            case _:
                # Handle invalid options
                print("Please choose a valid option from the menu.")
        input()

# Ending message to demonstrate the use of 'finally' block
try:
    # Ask the user for input and display a positive message if it's a number
    choice = int(input(
        "\nType a number to get a nice message, or anything else for a mean message: "))
    print("You look nice today")
except ValueError:
    # If input is not a number, display a different message
    print("I... I can't do this. You look way too nice today")
finally:
    # Always display this message, regardless of the input
    print("Anyway, thank you!")
