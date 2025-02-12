# Sum of all elements in a list using recursion
def list_sum(chosenList):
    if len(chosenList) == 1:
        # Base case: when there's only one element, return it
        return chosenList[0]
    else:
        # Add first element and recurse with the rest of the list
        return chosenList[0] + list_sum(chosenList[1:])


# Sum of numbers from 0 to N using recursion
def number_sum(chosenNumber):
    if chosenNumber == 1:
        return 1  # Base case: when the number is 1, return 1
    else:
        # Add number to the sum of numbers below it
        return chosenNumber + number_sum(chosenNumber - 1)


# GCD of two numbers using recursion
def gcd_calculator(x, y):
    if x >= y and x % y == 0:
        return y  # Base case: when x is divisible by y, return y
    elif x < y:
        return gcd_calculator(y, x)  # Swap x and y if x is less than y
    else:
        # Recurse with the remainder of x divided by y
        return gcd_calculator(y, x % y)


# Exponentiation of a number using recursion
def exp_calculator(x, y):
    if y == 0:
        return 1  # Base case: x^0 is 1
    elif y % 2 == 0:
        # Recurse with half the exponent
        half_power = exp_calculator(x, y // 2)
        # Multiply the half powers together for even exponents
        return half_power * half_power
    else:
        # Multiply x by the result of exp(x, y-1) for odd exponents
        return x * exp_calculator(x, y - 1)


# Finding number in list
def number_finder(chosenList, n):
    if len(chosenList) == 0:  # Base case: if the list is empty, return 0 (number not found)
        return 0
    # If the first element matches the number, count it and recurse for the rest of the list
    if chosenList[0] == n:
        return 1 + number_finder(chosenList[1:], n)
    # Recurse for the rest of the list if the first element doesn't match the number
    return number_finder(chosenList[1:], n)


# Function to get list input from the user
def get_list_input():
    yourList = []
    yourLength = int(input("Choose the desired length for your list: "))
    for i in range(0, yourLength):
        yourNumber = float(
            input(f"({i + 1}/{yourLength}) Choose a number to be added to your list: "))
        yourList.append(yourNumber)
    return yourList


# Function to calculate sum of all elements in a list
def sum_list():
    yourList = get_list_input()
    print(f"The sum of all numbers in the list is: {list_sum(yourList)}\n")


# Function to calculate sum of numbers from 0 to N
def sum_numbers():
    yourNumber = int(input("Choose a number: "))
    print(
        f"The sum of numbers from 0 to {yourNumber} is: {number_sum(yourNumber)}\n")


# Function to calculate GCD of two numbers
def find_gcd():
    yourX = int(input('Enter X\'s value: '))
    yourY = int(input('Enter Y\'s value: '))
    print(
        f"The GCD of {yourX} and {yourY} is: {gcd_calculator(yourX, yourY)}\n")


# Function to calculate exponentiation of a number
def calculate_exp():
    yourX = int(input('Enter base value: '))
    yourY = int(input('Enter exponent value: '))
    print(
        f"The result of {yourX}^{yourY} is: {exp_calculator(yourX, yourY)}\n")


# Function to find a number in a list
def find_number():
    yourList = get_list_input()
    yourNumber = int(input("Choose the number to be searched for: "))
    print(
        f"\nThe number {yourNumber} appears {number_finder(yourList, yourNumber)} time(s) in your list.\n")


# Menu function to allow user to select which function to run
def menu():
    while True:
        print("\nSelect an option:")
        print("1. Sum of all elements in a list")
        print("2. Sum of numbers from 0 to N")
        print("3. Find GCD of two numbers")
        print("4. Exponentiation of a number")
        print("5. Find number occurrences in a list")
        print("6. Exit")

        choice = input("Enter your choice: ")
        print()

        if choice == '1':
            sum_list()
        elif choice == '2':
            sum_numbers()
        elif choice == '3':
            find_gcd()
        elif choice == '4':
            calculate_exp()
        elif choice == '5':
            find_number()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select again.")


# Run the menu function
menu()
