# Sum of all elements in a list using recursion:
def list_sum(chosenList):
    if len(chosenList) == 1:
        return chosenList[0]  # Base case: when there's only one element, return it
    else:
        return chosenList[0] + list_sum(chosenList[1:])  # Add first element and recurse with the rest of the list

# Get list input from the user:
yourList = []
yourLength = int(input("Choose the desired length for your list: (Keep it short to make it easier to check!) "))

# Populate the list with user input:
for i in range(0, yourLength):
    yourNumber = float(input(f"({i + 1}/{yourLength}) Choose a number to be added to your list: "))
    yourList.append(yourNumber)

# Print the sum of the list:
print(f"The sum of all numbers in the list is: {list_sum(yourList)}\n")


# Sum of numbers from 0 to N using recursion:
def number_sum(chosenNumber):
    if chosenNumber == 1:
        return 1  # Base case: when the number is 1, return 1
    else:
        return chosenNumber + number_sum(chosenNumber - 1)  # Add number to the sum of numbers below it

# Get number input from the user:
yourNumber = int(input(f"Choose a number: "))

# Print the sum from 0 to the chosen number:
print(f"The sum of numbers from 0 to {yourNumber} is: {number_sum(yourNumber)}\n")


# GCD of two numbers using recursion:
def gcd_calculator(x, y):
    if x >= y and x % y == 0:
        return y  # Base case: when x is divisible by y, return y
    elif x < y:
        return gcd_calculator(y, x)  # Swap x and y if x is less than y
    else:
        return gcd_calculator(y, x % y)  # Recurse with the remainder of x divided by y

# Get user input for two numbers:
yourX = int(input('Enter X\'s value: '))
yourY = int(input('Enter Y\'s value: '))

# Print the GCD of the two numbers:
print(f"The GCD of {yourX} and {yourY} is: {gcd_calculator(yourX, yourY)}\n")


# Exponentiation of a number using recursion:
def exp_calculator(x, y):
    if y == 0:
        return 1  # Base case: x^0 is 1
    elif y % 2 == 0:
        half_power = exp_calculator(x, y // 2)  # Recurse with half the exponent
        return half_power * half_power  # Multiply the half powers together for even exponents
    else:
        return x * exp_calculator(x, y - 1)  # Multiply x by the result of exp(x, y-1) for odd exponents

# Get base and exponent input from the user:
yourX = int(input('Enter base value: '))
yourY = int(input('Enter exponent value: '))

# Print the result of exponentiation:
print(f"The result of {yourX}^{yourY} is: {exp_calculator(yourX, yourY)}\n")
